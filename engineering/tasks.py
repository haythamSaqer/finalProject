from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(email, name):
    """sends an email when feedback form is filled successfully"""
    print('hi*********************')

    send_mail('The note "' + name + '" has been read ',
              'his is an automatic notification to let you know that the note you created referred as "'
              + name + '" has been read and was destroyed immediately after.Do you want to send another note?',
              settings.EMAIL_HOST,
              [email])

