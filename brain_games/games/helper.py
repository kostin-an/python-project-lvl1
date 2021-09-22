import prompt
import random


def generate_number():
    return random.randint(1, 101)


def get_answer():
    return prompt.string('You answer: ')


def get_operation():
    operation_list = ['+', '-', '*']
    return random.choice(operation_list)
