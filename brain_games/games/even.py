from brain_games.games.helper import get_answer, get_check, \
    get_even_result, generate_number


def even_check(name="User"):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        number = generate_number()
        result = get_even_result(number)
        print(f'Question: {number}')
        answer = get_answer().lower()
        i = get_check(i, answer, result)
        if i == 3:
            print(f'Congratulations, {name}!')
        elif i == 4:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{result}\'')
            print(f'Let\'s try again, {name}!')
