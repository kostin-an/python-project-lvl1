from brain_games.engine import generate_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_round():
    number = generate_number()
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
