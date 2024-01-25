import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from accounts.models import User
from django.conf import settings




class Mailservice:
    def __init__(self,subject,recipient_list,message):
        self.subject=subject
        self.message=message
        self.from_email=settings.EMAIL_HOST_USER
        self.recipient_list=recipient_list
    def sendmail(self,template,context,*args,**kwargs):
        print(context)
        send_mail(self.subject,
                  self.message,
                  self.from_email,
                  self.recipient_list,
                  fail_silently=True,
                  html_message=render_to_string(template,context))
        
class UserPasswordResetEmail(Mailservice):
    domain="localhost:8000"
    def __init__(self,userid):
        self.userid=userid
        self.user=User.objects.get(id=self.userid)
        super(UserPasswordResetEmail,self).__init__(
                                        'New User',
                                        [self.user.email],
                                        f'Hi {self.user.username} welcome')
    def sendmail(self):
        context={"uid": urlsafe_base64_encode(force_bytes(self.userid)),
                "token": default_token_generator.make_token(self.user),
                "protocol":"http",
                "domain":self.domain}
        super().sendmail('user/password_reset_email.html',context=context)


