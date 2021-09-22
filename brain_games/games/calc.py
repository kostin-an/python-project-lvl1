from brain_games.games.helper import generate_number, get_answer, get_operation


def calc(name='User'):
    print('What is the result of the expression?')

    i = 0
    while i < 3:
        number_one = generate_number()
        number_two = generate_number()
        operation = get_operation()
        if operation == '+':
            result = int(number_one) + int(number_two)
        elif operation == '-':
            result = int(number_one) - int(number_two)
        else:
            result = int(number_one) * int(number_two)

        print(f'Question: {number_one} {operation} {number_two}')
        answer = get_answer()

        if answer == str(result):
            print('Correct!')
            i += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{result}\'')
            print(f'Let\'s try again, {name}!')
            break

    if i == 3:
        print(f'Congratulations, {name}!')
