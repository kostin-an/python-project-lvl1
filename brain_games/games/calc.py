from brain_games.games.helper import generate_number, get_answer, generate_operation, \
    get_calc_result, get_check


def calc(name='User'):
    print('What is the result of the expression?')

    i = 0
    while i < 3:
        number_one = generate_number()
        number_two = generate_number()
        operation = generate_operation()
        result = get_calc_result(number_one, number_two, operation)

        print(f'Question: {number_one} {operation} {number_two}')
        answer = get_answer()
        i = get_check(i, answer, result)
        if i == 3:
            print(f'Congratulations, {name}!')
        elif i == 4:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{result}\'')
            print(f'Let\'s try again, {name}!')
