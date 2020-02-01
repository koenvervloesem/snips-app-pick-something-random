# Pick something random app for Snips 

[![Build status](https://api.travis-ci.com/koenvervloesem/snips-app-pick-something-random.svg?branch=master)](https://travis-ci.com/koenvervloesem/snips-app-pick-something-random) [![Maintainability](https://api.codeclimate.com/v1/badges/b02b8ff9a4ebd13f9e3f/maintainability)](https://codeclimate.com/github/koenvervloesem/snips-app-pick-something-random/maintainability) [![Code quality](https://api.codacy.com/project/badge/Grade/178255b06d224fabb2aae5b83827de3f)](https://www.codacy.com/app/koenvervloesem/snips-app-pick-something-random) [![Python versions](https://img.shields.io/badge/python-3.5|3.6|3.7-blue.svg)](https://www.python.org) [![GitHub license](https://img.shields.io/github/license/koenvervloesem/snips-app-pick-something-random.svg)](https://github.com/koenvervloesem/snips-app-pick-something-random/blob/master/LICENSE) [![Languages](https://img.shields.io/badge/i18n-en|fr-brown.svg)](https://github.com/koenvervloesem/snips-app-pick-something-random/tree/master/translations) [![Snips App Store](https://img.shields.io/badge/snips-app-blue.svg)](https://console.snips.ai/store/en/skill_NmlgOeBBO13)

**Important information: Following the acquisition of Snips by Sonos, the Snips Console is not available anymore after January 31, 2020. As such, I have exported all data of the English version of this app from the Snips Console and made these available in the directory [console](https://github.com/koenvervloesem/snips-app-pick-something-random/tree/master/console) with the same MIT license as the rest of this project. This project has been archived. If you're searching for an alternative to Snips, I believe that [Rhasspy](https://rhasspy.readthedocs.io/) is currently the best choice for an offline open source voice assistant.**

With this [Snips](https://snips.ai/) app, you can ask for random numbers and dates, to flip a coin and to roll a die or multiple dice.

## Installation

The easiest way to install this app is by adding the Snips app to your assistant in the [Snips Console](https://console.snips.ai):

*   English: [Pick something random](https://console.snips.ai/store/en/skill_NmlgOeBBO13)
*   French: [Choix aléatoire](https://console.snips.ai/store/fr/skill_9Y1Avk694al)

## Usage

This app recognizes the following intents:

*   FlipCoin - The user asks to flip a coin. The app reasponds with heads or tails.
*   RandomNumber - The user asks to pick a random number between two numbers. The app responds with a number.
*   RandomDate - The user asks to pick a random date, optionally in a specific period. The app responds with a date in the specified time period.
*   RollDice - The user asks to roll a die or multiple dice (specified in words or in [dice notation](https://en.wikipedia.org/wiki/Dice_notation)). The app responds with the numbers.

## Copyright

This app is provided by [Koen Vervloesem](mailto:koen@vervloesem.eu) as open source software. See LICENSE for more information.
