"""
This module contains the result sentences and intents for the English version
of the Pick something random app.
"""

# Result sentences and their parts:
RESULT_HEADS = "Heads"
RESULT_TAILS = "Tails"
# See the following documentation for the format codes:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
RESULT_MONTH_DAY = "%B %-d"
RESULT_DATE_ALREADY_PICKED = "It looks like you already picked a date. Are you trying to trick me?"
RESULT_NUMBERS_WRONG_ORDER = "Is this a trick? {} is smaller than {}."
RESULT_ONE_NUMBER = "It looks like you already picked a number. Are you trying to trick me?"
RESULT_TOO_MANY_DICE = "I'm sorry but I don't have {} dice to roll."
RESULT_NEGATIVE_DICE = "Are you trying to trick me? I can't throw a negative number of dice, obviously."
RESULT_ZERO_DICE = "I threw zero dice. Have you heard them fall?"
RESULT_DICE_NO_INTEGER = "Are you trying to trick me? I can't throw a non-integer number of dice, obviously."
RESULT_FACES_NO_INTEGER = "Are you trying to trick me? I can't throw dice with a non-integer number of faces, obviously."
RESULT_ZERO_FACES = "I threw a die with zero faces. Have you seen its number?"
RESULT_NEGATIVE_FACES = "Are you trying to trick me? I can't throw dice with a negative number of faces, obviously."
AND = ", and "

# Intents
INTENT_FLIP_COIN = 'koan:FlipCoin'
INTENT_RANDOM_DATE = 'koan:RandomDate'
INTENT_RANDOM_NUMBER = 'koan:RandomNumber'
INTENT_ROLL_DICE = 'koan:RollDice'
