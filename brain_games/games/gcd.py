from brain_games.games.helper import generate_number, get_answer, \
    get_check, get_gcd_result


def gcd(name='User'):
    print('Find the greatest common divisor of given numbers.')

    i = 0
    while i < 3:
        number_one = generate_number()
        number_two = generate_number()
        result = get_gcd_result(number_one, number_two)

        print(f'Question: {number_one} {number_two}')
        answer = get_answer()
        i = get_check(i, answer, result)
        if i == 3:
            print(f'Congratulations, {name}!')
        elif i == 4:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{result}\'')
            print(f'Let\'s try again, {name}!')
