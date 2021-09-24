import random

from brain_games.games.helper import generate_progression, get_answer, get_check


def progression(name="User"):
    print('What number is missing in the progression?')

    i = 0
    while i < 3:
        progression_user = generate_progression()
        index = random.randint(0, len(progression_user) - 1)
        progression_quest = progression_user.copy()
        progression_quest[index] = '..'
        progression_str = ", ".join(map(str, progression_quest))

        print(f'Question: {progression_str}')
        answer = get_answer()
        i = get_check(i, answer, progression_user[index])
        if i == 3:
            print(f'Congratulations, {name}!')
        elif i == 4:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{progression_user[index]}\'')
            print(f'Let\'s try again, {name}!')
