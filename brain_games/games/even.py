from brain_games.engine import generate_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    number = generate_number()
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(number), str(correct_answer)
