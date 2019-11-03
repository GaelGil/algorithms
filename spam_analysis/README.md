# Spam Analysis

These are instructions from Cameron. After you've completed the project, edit this README so that it becomes an actual `README` instead of instructions.

## Overview

Build an algorithm that can accurately detect which SMS messages are spam.

## Dataset

The data comes from the [UC Irvine SMS Spam Collection Data Set](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection). This data has two columns separated by a tab. The first column tells whether the SMS message is spam or legitimate ("ham").

Cameron took this file and divided it into two parts. You (Gael) get to look at the first part and use it to design your algorithm. This data is saved in `data/train`. I've kept the second part secret (well, not very secret... it's in `data/.test` -- but don't look at it!). After you make your algorithm I'll use the test dataset to see how accurate it is. Looking at the test set is cheating. There are 4574 rows in the training dataset and 1000 in the test set.

## Process

Notes from Cameron:

- The _API_ of your algorithm should be a function that simply accepts an SMS message as a string and outputs either one of two values: `"ham"` or `"spam`:

~~~python
def bad_algorithm_v1(input: str) -> str:
    """
    Bad algorithm that returns "ham" for everythig.
    """
    return "ham"

