from question.models import Question


def get_all_questions():
    """Returns all questions"""
    questions = Question.objects.order_by('-created_at')
    return questions
