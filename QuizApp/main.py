from question_model import Question
from data import fetch_questions
from ui import get_user_quiz_settings
from quiz_brain import QuizBrain
from quiz_interface_model import QuizInterface

user_settings = get_user_quiz_settings()
question_data = fetch_questions(user_settings)
question_bank = [
    Question(q["question"], q["correct_answer"])
    for q in question_data
]

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")