import csv
from question_model import Question
from quiz_control import QuizControl

questions = []

# Write your code below #
level = input('Select difficulty (easy, medium, hard): ')
with open('questions.csv', 'r') as data_file:
    row = csv.DictReader(data_file)
    for r in row:
        if r['difficulty'] == level:
            questions.append(r)

# Write your code above #

quiz = QuizControl(questions)
while quiz.has_question():
    quiz.next()
