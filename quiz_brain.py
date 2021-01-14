class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def proceed_to_next_question(self):
        i = self.question_number
        text = self.question_list[i].text
        correct_answer = self.question_list[i].answer.lower()
        user_answer = input(f"Q.{i + 1}: {text} (True/False)?: ").lower()

        self.question_number += 1
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it!")
            self.score += 1
        else:
            print("Wrong answer.")

        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
