#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a Snips skill that lets you ask for random numbers,
coin flips, dates and dice rolls.
"""

import random
from datetime import date

from hermes_python.ontology.dialogue import InstantTimeValue, TimeIntervalValue
from snipskit.apps import HermesSnipsApp
from snipskit.decorators.hermes import intent
import tools_pick_something_random as tools

# Dice characteristics
MAX_DICE = 10  # The maximum number of dice the skill will roll.
DICE_FACES = 6  # The number of faces on the dice.

# Result sentences and their parts:
RESULT_HEADS = "Heads"
RESULT_TAILS = "Tails"
RESULT_MONTH_DAY = "%B %-d"
RESULT_DATE_ALREADY_PICKED = "It looks like you already picked a date. Are you trying to trick me?"
RESULT_NUMBERS_WRONG_ORDER = "Is this a trick? {} is smaller than {}."
RESULT_ONE_NUMBER = "It looks like you already picked a number. Are you trying to trick me?"
RESULT_TOO_MANY_DICE = "I'm sorry but I don't have {} dice to roll."
RESULT_NEGATIVE_DICE = "Are you trying to trick me? I can't throw a negative number of dice, obviously."
RESULT_ZERO_DICE = "I threw zero dice. Have you heard them fall?"
RESULT_DICE_NO_INTEGER = "Are you trying to trick me? I can't throw a non-integer number of dice, obviously."
AND = ", and "


class PickSomethingRandom(HermesSnipsApp):
    """This skill lets you ask for random numbers."""

    def initialize(self):
        """Initialize the skill."""

        random.seed()

    @intent('koan:FlipCoin')
    def flip_coin_callback(self, hermes, intent_message):
        """Callback for intent FlipCoin"""

        result_sentence = random.choice([RESULT_HEADS, RESULT_TAILS])

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent('koan:RollDice')
    def roll_dice_callback(self, hermes, intent_message):
        """Callback for intent RollDice"""

        result_sentence = ""
        if intent_message.slots.amount:
            # The user specified an amount of dice
            amount = intent_message.slots.amount.first().value
            if not amount.is_integer():
                # Not an integer number
                result_sentence = RESULT_DICE_NO_INTEGER
            elif amount > MAX_DICE:
                # Too many dice
                result_sentence = RESULT_TOO_MANY_DICE.format(int(amount))
            elif amount == 0:
                # No dice
                result_sentence = RESULT_ZERO_DICE
            elif amount < 0:
                # Negative number of dice
                result_sentence = RESULT_NEGATIVE_DICE
            else:
                # And finally a sensible number of dice...
                dice_rolls = [str(random.randint(1, DICE_FACES))
                              for number in range(0, int(amount))]
                last = dice_rolls.pop()
                result_sentence = ", ".join(dice_rolls) + AND + last
        else:
            # Roll one die
            result_sentence = str(random.randint(1, DICE_FACES))

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent('koan:RandomNumber')
    def random_number_callback(self, hermes, intent_message):
        """Callback for intent RandomNumber"""

        result_sentence = ""

        min_number = intent_message.slots.min.first().value
        max_number = intent_message.slots.max.first().value

        if min_number == max_number:
            result_sentence = RESULT_ONE_NUMBER
        elif min_number > max_number:
            result_sentence = RESULT_NUMBERS_WRONG_ORDER.format(max_number,
                                                                min_number)
        else:
            result_sentence = str(random.randint(min_number, max_number))

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    @intent('koan:RandomDate')
    def random_date_callback(self, hermes, intent_message):
        """Callback for intent RandomDate"""

        result_sentence = ""

        if intent_message.slots.period:
            # The user specified a snips/datetime entity.
            period = intent_message.slots.period.first()
            if isinstance(period, InstantTimeValue):
                # Test the grain of the 'instant' time value.
                (start_date, end_date) = tools.get_period_from_grainy_time(period)
                if start_date == end_date:
                    # There's no date to pick, the user already picked one :-)
                    result_sentence = RESULT_DATE_ALREADY_PICKED
                else:
                    result_sentence = tools.random_date(start_date, end_date).strftime(RESULT_MONTH_DAY)
            elif isinstance(period, TimeIntervalValue):
                # The user explicitly specified a time period.
                # TODO: What if from_date or to_date are missing?
                start_date = tools.string_to_date(period.from_date)
                end_date = tools.string_to_date(period.to_date)
                result_sentence = tools.random_date(start_date, end_date).strftime(RESULT_MONTH_DAY)
        else:
            # The user didn't specify any time period, so we return a random month and day.
            # Choose a leap year so February 29 is a possible result.
            start_date = date(2016, 1, 1)
            end_date = date(2016, 12, 31)
            result_sentence = tools.random_date(start_date, end_date).strftime(RESULT_MONTH_DAY)

        hermes.publish_end_session(intent_message.session_id, result_sentence)


if __name__ == "__main__":
    PickSomethingRandom()
