from question_model import *
from data import *
from quiz_brain import *

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the challenge!")
print(f"Your final score is {quiz_brain.score}/{len(question_bank)}")