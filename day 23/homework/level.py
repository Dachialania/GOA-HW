
def arithmetic_operations(a, b):

    if b == 0:
        division = 'undefined (division by zero)'
        modulus = 'undefined (modulus by zero)'
    else:
        division = a / b
        modulus = a % b
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': division,
        'modulus': modulus
    }


def add_until_100(a, b):
    while a < 100:
        a += b
    return a

def is_even_or_odd(number):
    return 'even' if number % 2 == 0 else 'odd'


def find_max_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)


def sum_of_list(numbers):
    return sum(numbers)

def reverse_sequence(*args):
    return list(args)[::-1]

def longest_and_shortest(strings):
    if not strings:
        return None, None
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    return longest, shortest

def swap_case(s):
    return s.swapcase()

def count_consonants(s):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in s if char in consonants)


def is_even(number):
    return number % 2 == 0



def sum_even_index(numbers):
    total = 0
    for i in range(0, len(numbers), 2): 
        total += numbers[i]
    return total


def is_even_or_odd(number):
    return 'even' if number % 2 == 0 else 'odd'


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def capitalize_names(names):
    return [name.capitalize() for name in names]


def transform_numbers(numbers):
    transformed = []
    for number in numbers:
        if number % 2 == 0: 
            transformed.append(number / 2)
        else: 
            transformed.append(number * 2)
    return transformed
