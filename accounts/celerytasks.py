from celery import shared_task
from service.mailservice import Mailservice
from django.conf import settings


@shared_task
def mailsender(email,username):
    Mailservice(subject='New User',
                message=f"Hi {username} welcome to PM reset your password and sign",
                recipient_list=[email],
                from_email=settings.EMAIL_HOST_USER).sendmail()