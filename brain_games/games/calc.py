import random
from brain_games.engine import generate_number


DESCRIPTION = 'What is the result of the expression?'


def generate_operation():
    operation_list = ['+', '-', '*']
    return random.choice(operation_list)


def get_round():
    number_one = generate_number()
    number_two = generate_number()
    operation = generate_operation()
    question = f'{number_one} {operation} {number_two}'
    if operation == '+':
        correct_answer = int(number_one) + int(number_two)
    elif operation == '-':
        correct_answer = int(number_one) - int(number_two)
    else:
        correct_answer = int(number_one) * int(number_two)
    return question, str(correct_answer)
