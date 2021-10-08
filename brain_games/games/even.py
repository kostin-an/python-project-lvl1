from brain_games.engine import generate_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_round():
    number = generate_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer
