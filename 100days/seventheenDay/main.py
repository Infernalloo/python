from question_model import *
from data import *
from quiz_brain import *

question_bank = []

for dictionary in question_data:
    q_text = dictionary["text"]
    q_answer = dictionary["answer"]
    new_question = Question(text=q_text, answer=q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()