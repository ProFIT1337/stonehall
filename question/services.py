from question.models import Question


def get_all_questions():
    """Returns all questions"""
    questions = Question.objects.order_by('-created_at')
    return questions


def get_question_with_pk(pk:int):
    """Returns question with pk"""
    question = Question.objects.get(pk=pk)
    return question

def get_qty_unanswered_feedback() -> int:
    """Returns the number of questions with an argument 'is_answered'==False"""
    qty = 0
    questions = get_all_questions()
    for question in questions:
        if not question.is_answered:
            qty += 1
    return qty
