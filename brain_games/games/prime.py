from brain_games.engine import generate_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_prime_result(number):
    if number < 2:
        return 'no'
    list_number = list(range(1, number))
    for i in list_number:
        if (i > 1) and (number % i == 0):
            return 'no'
    return 'yes'


def get_round():
    number = generate_number()
    question = str(number)
    correct_answer = get_prime_result(number)
    return question, correct_answer
