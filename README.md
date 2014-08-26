# WTP Temp Unit Generator

[![Build Status](https://travis-ci.org/PlasmaSheep/wtp-temp-unit-generator.svg?branch=develop)](https://travis-ci.org/PlasmaSheep/wtp-temp-unit-generator)
[![Code Health](https://landscape.io/github/PlasmaSheep/wtp-temp-unit-generator/master/landscape.png)](https://landscape.io/github/PlasmaSheep/wtp-temp-unit-generator/master)

In my comp civics class we had six teams, each studying their own specific area.
In the beginning of the year, our teacher would divide the class into six
units and all six units would do the same topic for a week. For six weeks, we
cycled through each topic, every time being put into a "temp unit" with
different people, the goal being to work with as many people as possible.

However, our teacher had a problem - it was a hassle to manually try to
maximize individual collaborations. So I decided to take a look at the problem.
I figured out a decent algorithm and implemented it in python for easy use,
hopefully sparing my teacher some wasted time.

## Installation

If you just want to run the generator, you don't need to install anything except
for [python 3](https://www.python.org/downloads).

If you want to run the tests:

    pip install -r requirements.txt
    nosetests

## Use

1. Clone this repository, or if you don't have git, just use the download link
    on the right.

        git clone https://github.com/PlasmaSheep/wtp-temp-unit-generator.git

    If you downloaded from the zip, you'll have to unzip it.

2. Navigate to the downloaded directory, then in the terminal run:

        python3 rungenerator.py

