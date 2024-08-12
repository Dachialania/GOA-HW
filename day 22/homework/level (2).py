
def add_five(number):
    return number + 5

def multiply_two_numbers(a, b):
    return a * b


def string_length(s):
    return len(s)


def lengths_of_strings(strings):
    return [len(s) for s in strings]

def is_palindrome(s):
    return s == s[::-1]

    if not strings:
        return None
    return max(strings, key=len)

import math
def factorial(n):
    return math.factorial(n)

def sum_of_max_values(list1, list2):
    if not list1 or not list2:
        return None
    return max(list1) + max(list2)


def difference_of_min_values(list1, list2):
    if not list1 or not list2:
        return None
    return abs(min(list1) - min(list2))


def range_of_list(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)



def sum_of_list(numbers):
    return sum(numbers)


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def square_elements(numbers):
    return [x ** 2 for x in numbers]


def reverse_string(s):
    return s[::-1]


def is_even(number):
    return number % 2 == 0


def longest_string(strings):
    if not strings:
        return None
    return max(strings, key=len)


def smallest_number(numbers):
    if not numbers:
        return None
    return min(numbers)


import math
def gcd(a, b):
    return math.gcd(a, b)


def to_uppercase(s):
    return s.upper()


def average_of_list(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
