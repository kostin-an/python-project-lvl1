import math
import prompt
import random


def generate_number():
    return random.randint(1, 101)


def get_answer():
    return prompt.string('You answer: ')


def generate_operation():
    operation_list = ['+', '-', '*']
    return random.choice(operation_list)


def generate_progression():
    start = random.randint(1, 5)
    step = random.randint(1, 5)
    stop = step * 10
    progression_list = list(range(start, stop, step))
    return progression_list


def get_even_result(number):
    if (number % 2) == 0:
        return 'yes'
    else:
        return 'no'


def get_calc_result(number_one, number_two, operation):
    if operation == '+':
        result = int(number_one) + int(number_two)
    elif operation == '-':
        result = int(number_one) - int(number_two)
    else:
        result = int(number_one) * int(number_two)
    return result


def get_gcd_result(number_one, number_two):
    return math.gcd(number_one, number_two)


def get_check(i, answer, result):
    if answer == str(result):
        print('Correct!')
        i += 1
    else:
        i = 4
    return i
