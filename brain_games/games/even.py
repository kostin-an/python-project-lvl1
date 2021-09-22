import random
import prompt


def even_check(name="User"):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 101)
        result = number % 2
        print(f'Question: {number}')
        answer = prompt.string('You answer: ')
        if (result == 0 and answer.lower() == 'yes') or (result == 1 and answer.lower() == 'no'):
            print("Correct!")
            i += 1
        elif answer.lower() == 'yes':
            print(f'\'yes\' is wrong answer ;(. '
                  f'Correct answer was \'no\'.\nLet\'s try again, {name}!')
            break
        elif answer.lower() == 'no':
            print(f'\'no\' is wrong answer ;(. '
                  f'Correct answer was \'yes\'.\nLet\'s try again, {name}!')
            break
        else:
            print(f'\'{answer}\' is wrong answer ;(.\nLet\'s try again, {name}!')
            break
    if i == 3:
        print(f'Congratulations, {name}!')
