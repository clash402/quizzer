from data import data
from question import Question
from quiz_brain import QuizBrain


# MAIN
question_bank = [Question(q["text"], q["answer"]) for q in data]
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.proceed_to_next_question()

print("Quiz complete.")
print(f"Your final score is {quiz_brain.score}/{len(quiz_brain.question_list)}")
