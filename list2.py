#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: List2
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = (
    """
    manuel Velasco
    "https://stackoverflow.com/questions/7237875/linear-merging-for-lists-in-python"
    "https://stackoverflow.com/questions/16096754/remove-none-value-from-a-list-without-removing-the-0-value"
    Amanda help with remove_adjacent and zip_merge
    """
)

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# D. remove_adjacent
# Given a list of numbers, return a list where all adjacent
# equal elements have been reduced to a single element.
# Example:
#   [1, 2, 2, 3] -> [1, 2, 3]
# You may create a new list or modify the passed in list.
# Hint: Don't use set()


def remove_adjacent(num):
    zero = 0
    while zero < len(num):
        if num[zero] == num[zero-1]:
            num.pop(zero)
            zero -= 1
        else:
            zero += 1
            # print(num)
    return num


# E. zip_merge
# Given two lists, combine the values from their corresponding
# indices into a single list.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = ['My', 'name', 'is', 'Kelly']
# Hint: Think of it as "zipping" two lists together.  Is there
# a built-in function in python that will do this?


def zip_merge(list1, list2):
    kelly = list(zip(list1, list2))
    sent = []
    for item in kelly:
        sent.append(''.join(item))
    return sent

    # F. empty_filter
    # Given a single list containing strings, empty strings, and
    # None values:  Return a new list with the same elements, but
    # strip out (filter) the empty strings and None values away.
    # example: list1 = ["Mike", "", "Emma", None, "Kelly", "", "Brad", None]
    # result:  ["Mike", "Emma", "Kelly", "Brad"]
    # Hint: There is a Python idiom for doing this.  Can you find it?


def empty_filter(list1):
    # none_list = list(filter(partial(is_not, None), list1))
    # return list(filter(partial(is_not, ""), none_list))
    # return list(filter(lambda x: x is not "" and x is not None, list1))
    return list(filter(None and ''.__ne__, list1))
    #
    #

    #

    # G. linear_merge
    # Given two lists sorted in increasing order, create and
    # return a merged list of all the elements in sorted order.
    # You may modify the passed in lists.
    # The solution should work in "linear" time, making a single
    # pass of both lists.
    # Hint: Don't use `sort` or `sorted` -- they are not O(n)
    # linear time and the two lists are already provided in
    # ascending sorted order.


def linear_merge(list1, list2):
    list1.extend(list2)
    print(sorted(list1))

    return sorted(list1)

    # Provided simple test() function used in main() to print
    # what each function returns vs. what it's supposed to return.


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.
def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.

    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('\nlinear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

    print('\nzip_merge')
    test(zip_merge(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"]),
         ['My', 'name', 'is', 'Kelly'])

    print('\nempty_filter')
    test(empty_filter(["Mike", "", "Emma", None, "Kelly", "", "Brad", None]),
         ["Mike", "Emma", "Kelly", "Brad"])


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
