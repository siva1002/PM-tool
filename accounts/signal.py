# blog/signals.py
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .celerytasks import mailsender
User=get_user_model()
# Define the signal

@receiver(post_save,sender=User)
def send_notification(sender,instance, **kwargs):
    mailsender.delay(instance.id)