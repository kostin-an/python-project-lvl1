import math
from brain_games.engine import generate_number


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round():
    number_one = generate_number()
    number_two = generate_number()
    question = f'{number_one} {number_two}'
    correct_answer = math.gcd(number_one, number_two)
    return question, str(correct_answer)
