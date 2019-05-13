"""
This module contains the result sentences and intents for the French version
of the Pick something random app.
"""

# Result sentences and their parts:
RESULT_HEADS = "Pile"
RESULT_TAILS = "Face"
# See the following documentation for the format codes:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
RESULT_MONTH_DAY = "D MMMM"
RESULT_DATE_ALREADY_PICKED = "On dirait que vous avez déjà choisi une date. Essayez-vous de me piéger?"
RESULT_NUMBERS_WRONG_ORDER = "Est-ce un piège? {} est plus petit que {}."
RESULT_ONE_NUMBER = "On dirait bien que vous avez déjà choisi un nombre. Essayez-vous de me piéger?"
RESULT_TOO_MANY_DICE = "Je suis désolé mais je n'ai pas {} dés à lancer."
RESULT_NEGATIVE_DICE = "Essayez-vous de me piéger? Je ne peux évidemment pas lancer un nombre négatif de dés."
RESULT_ZERO_DICE = "J'ai jeté zéro dé. Les avez-vous entendus tomber?"
RESULT_DICE_NO_INTEGER = "Essayez-vous de me piéger? Je ne peux évidemment pas lancer des dés avec un nombre non entier."
RESULT_FACES_NO_INTEGER = "Essayez-vous de me piéger? Je ne peux évidemment pas lancer des dés avec un nombre de faces non entier."
RESULT_ZERO_FACES = "J'ai jeté un dé avec zéro face. Avez-vous vu son numéro?"
RESULT_NEGATIVE_FACES = "Essayez-vous de me piéger? Je ne peux évidemment pas lancer des dés avec un nombre de faces négatif."
AND = ", et "

# Intents
INTENT_FLIP_COIN = 'Sanlokii:FlipCoin'
INTENT_RANDOM_DATE = 'Sanlokii:RandomDate'
INTENT_RANDOM_NUMBER = 'Sanlokii:RandomNumber'
INTENT_ROLL_DICE = 'Sanlokii:RollDice'
