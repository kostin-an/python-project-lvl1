import random


DESCRIPTION = 'What number is missing in the progression?'
START_PROGRESSION = random.randint(1, 5)
STEP_PROGRESSION = random.randint(1, 5)
STOP_PROGRESSION = STEP_PROGRESSION * 10


def generate_progression():
    return list(range(START_PROGRESSION, STOP_PROGRESSION, STEP_PROGRESSION))


def transform_progression_to_string_for_question(progression, hole_index):
    progression_question = progression.copy()
    progression_question[hole_index] = '..'
    return " ".join(map(str, progression_question))


def get_round():
    progression = generate_progression()
    hole_index = random.randint(0, len(progression) - 1)
    question = transform_progression_to_string_for_question(progression, hole_index)
    correct_answer = str(progression[hole_index])
    return question, correct_answer
