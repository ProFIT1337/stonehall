from question.models import Question


def get_all_questions():
    """Returns all questions"""
    questions = Question.objects.order_by('-created_at')
    return questions


def get_question_with_pk(pk:int):
    """Returns question with pk"""
    question = Question.objects.get(pk=pk)
    return question