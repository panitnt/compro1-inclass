import random
from question_model import Question


class QuizControl:
    def __init__(self, question_list):
        # Write your code here
        self.question_list = question_list
        self.count_point = 0
        self.problem = 0

    def has_question(self):
        # Write your code here
        total_question = len(self.question_list)
        if self.problem == total_question:
            return False
        problem_i = self.question_list[self.problem]
        question = problem_i['question']
        correct_answer, incorrect_0 = problem_i['correct_answer'], problem_i['incorrect_answers/0']
        incorrect_1, incorrect_2 = problem_i['incorrect_answers/1'], problem_i['incorrect_answers/2']
        problem_class = Question(question, correct_answer, incorrect_0, incorrect_1, incorrect_2)
        choice = [problem_class.answer, problem_class.incorrect_0, problem_class.incorrect_1, problem_class.incorrect_2]
        random.shuffle(choice)
        print(f"Question: {problem_class.question}")
        for j in range(len(choice)):
            print(f'Choice {j + 1}: {choice[j]}')
        ans = int(input('Answer: '))
        ans_choice_input = choice[ans - 1]
        if problem_class.answer == ans_choice_input:
            print("That's correct.")
            self.count_point += 1
        else:
            print("That's wrong.")
            print(f"The correct answer is {problem_i['correct_answer']}")
        print(f"Your score is: {self.count_point}/{len(self.question_list)}")
        print()
        return True

    def next(self):
        # Write your code here
        self.problem += 1

    # You can create new method as if you want.
