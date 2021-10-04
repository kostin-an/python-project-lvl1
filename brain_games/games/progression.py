import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 5)
    step = random.randint(1, 5)
    stop = step * 10
    progression_list = list(range(start, stop, step))
    return progression_list


def get_round():
    progression = generate_progression()
    index = random.randint(0, len(progression) - 1)
    progression_question = progression.copy()
    progression_question[index] = '..'
    question = " ".join(map(str, progression_question))
    correct_answer = str(progression[index])
    return question, correct_answer
