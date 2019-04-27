#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a Snips app that lets you ask for random numbers,
coin flips, dates and dice rolls.
"""

import importlib
import json
from datetime import date
import random

from hermes_python.hermes import Hermes
from hermes_python.ontology.dialogue import InstantTimeValue, TimeIntervalValue
import tools_pick_something_random as tools
import toml

# Dice characteristics
MAX_DICE = 10  # The maximum number of dice the app will roll.
DICE_FACES = 6  # The default number of faces on the dice.


class PickSomethingRandom(object):
    """This Snips app lets you ask for random numbers."""

    def __init__(self):
        """Initialize the app."""

        random.seed()

        # Use the assistant's language.
        with open("/usr/share/snips/assistant/assistant.json") as json_file:
            language = json.load(json_file)["language"]

        self.i18n = importlib.import_module("translations." + language)

        # start listening to MQTT
        self.start_blocking()

    def flip_coin_callback(self, hermes, intent_message):
        """Callback for intent FlipCoin"""

        result_sentence = random.choice([self.i18n.RESULT_HEADS, self.i18n.RESULT_TAILS])

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    def roll_dice_callback(self, hermes, intent_message):
        """Callback for intent RollDice"""

        result_sentence = ""

        # Check the number of faces
        if intent_message.slots and intent_message.slots.faces:
            # The user specified an amount of faces
            faces = intent_message.slots.faces.first().value
            if not faces.is_integer():
                # Not an integer number
                result_sentence = self.i18n.RESULT_FACES_NO_INTEGER
            elif faces == 0:
                # No faces
                result_sentence = self.i18n.RESULT_ZERO_FACES
            elif faces < 0:
                # Negative number of faces
                result_sentence = self.i18n.RESULT_NEGATIVE_FACES
        else:
            # Take the default number of faces
            faces = DICE_FACES

        # If the number of faces is invalid, say an error message
        if result_sentence:
            hermes.publish_end_session(intent_message.session_id, result_sentence)
        else:

            if intent_message.slots and intent_message.slots.amount:
                # The user specified an amount of dice
                amount = intent_message.slots.amount.first().value
                if not amount.is_integer():
                    # Not an integer number
                    result_sentence = self.i18n.RESULT_DICE_NO_INTEGER
                elif amount > MAX_DICE:
                    # Too many dice
                    result_sentence = self.i18n.RESULT_TOO_MANY_DICE.format(int(amount))
                elif amount == 0:
                    # No dice
                    result_sentence = self.i18n.RESULT_ZERO_DICE
                elif amount < 0:
                    # Negative number of dice
                    result_sentence = self.i18n.RESULT_NEGATIVE_DICE
                else:
                    # And finally a sensible number of dice...
                    dice_rolls = [str(random.randint(1, faces))
                                  for number in range(0, int(amount))]
                    last = dice_rolls.pop()
                    result_sentence = ", ".join(dice_rolls) + self.i18n.AND + last
            else:
                # Roll one die
                result_sentence = str(random.randint(1, faces))

            hermes.publish_end_session(intent_message.session_id, result_sentence)

    def random_number_callback(self, hermes, intent_message):
        """Callback for intent RandomNumber"""

        min_number = intent_message.slots.min.first().value
        max_number = intent_message.slots.max.first().value

        if min_number == max_number:
            result_sentence = self.i18n.RESULT_ONE_NUMBER
        elif min_number > max_number:
            result_sentence = self.i18n.RESULT_NUMBERS_WRONG_ORDER.format(max_number,
                                                                          min_number)
        else:
            result_sentence = str(random.randint(min_number, max_number))

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    def random_date_callback(self, hermes, intent_message):
        """Callback for intent RandomDate"""

        if intent_message.slots and intent_message.slots.period:
            # The user specified a snips/datetime entity.
            period = intent_message.slots.period.first()
            if isinstance(period, InstantTimeValue):
                # Test the grain of the 'instant' time value.
                (start_date, end_date) = tools.get_period_from_grainy_time(period)
                if start_date == end_date:
                    # There's no date to pick, the user already picked one :-)
                    result_sentence = self.i18n.RESULT_DATE_ALREADY_PICKED
                else:
                    result_sentence = tools.random_date(start_date, end_date).strftime(self.i18n.RESULT_MONTH_DAY)
            elif isinstance(period, TimeIntervalValue):
                # The user explicitly specified a time period.
                # TODO: What if from_date or to_date are missing?
                start_date = tools.string_to_date(period.from_date)
                end_date = tools.string_to_date(period.to_date)
                result_sentence = tools.random_date(start_date, end_date).strftime(self.i18n.RESULT_MONTH_DAY)
        else:
            # The user didn't specify any time period, so we return a random month and day.
            # Choose a leap year so February 29 is a possible result.
            start_date = date(2016, 1, 1)
            end_date = date(2016, 12, 31)
            result_sentence = tools.random_date(start_date, end_date).strftime(self.i18n.RESULT_MONTH_DAY)

        hermes.publish_end_session(intent_message.session_id, result_sentence)

    def master_callback(self, hermes, intent_message):
        """
        Master callback function, triggered everytime an intent is recognized.
        """
        coming_intent = intent_message.intent.intent_name
        if coming_intent == self.i18n.INTENT_FLIP_COIN:
            self.flip_coin_callback(hermes, intent_message)
        elif coming_intent == self.i18n.INTENT_RANDOM_DATE:
            self.random_date_callback(hermes, intent_message)
        elif coming_intent == self.i18n.INTENT_RANDOM_NUMBER:
            self.random_number_callback(hermes, intent_message)
        elif coming_intent == self.i18n.INTENT_ROLL_DICE:
            self.roll_dice_callback(hermes, intent_message)

    def start_blocking(self):
        """Register callback function and start MQTT"""
        # Get the MQTT host and port from /etc/snips.toml.
        try:
            mqtt_addr = toml.load('/etc/snips.toml')['snips-common']['mqtt']
        except KeyError:
            # If the mqtt key doesn't exist, use the default value.
            mqtt_addr = 'localhost:1883'

        with Hermes(mqtt_addr) as hermes:
            hermes.subscribe_intents(self.master_callback).start()


if __name__ == "__main__":
    PickSomethingRandom()
