from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for question in question_data:
    text=question["text"]
    answer=question["answer"]
    new_question=Question(text,answer)
    question_bank.append(new_question)
quiz=Quizbrain(question_bank)
while quiz.stil_has_questionl():
    quiz.next_question()



