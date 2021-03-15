from django.core.mail import send_mail

from stonehall import settings


def send_notification_about_feedback(question):
    """Send notification about new feedback on admin email"""
    mail_subject = f'Новый вопрос от {question.sender_name}'
    mail_text = f"""
        На сайте отправили новый фидбек:
        Тема: {question.feedback_subject}
        Текст: {question.feedback_text}
        Конктная информация: {question.sender_contact_information}
    """
    send_mail(
        mail_subject,
        mail_text,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_TO],
        fail_silently=False
    )
