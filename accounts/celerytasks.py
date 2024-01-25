from celery import shared_task
from service.mailservice import UserPasswordResetEmail


@shared_task
def mailsender(userid):
    UserPasswordResetEmail(userid).sendmail()