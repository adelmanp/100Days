#!/usr/bin/python3

import random
from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain



questions_objects = []
more_questions = True

for q_a in question_data:
    q = q_a['text']
    a = q_a['answer']
    new_q = Questions(q, a)
    questions_objects.append(new_q)

quiz_brain = QuizBrain(questions_objects)


while more_questions:
    quiz_brain.next_question()
    more_questions = quiz_brain.still_has_questions()

print("You have completed the quiz")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")

