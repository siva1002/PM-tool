import datetime
import logging
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,redirect
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib import messages


logger = logging.getLogger(__name__)
User=get_user_model()


def index(request):
    logger.warning(
        "Homepage was accessed at " + str(datetime.datetime.now()) + " hours!"
    )
    return render(request, "index.html")


def page1(request):
    return render(request, "page1.html")



class ResetPasswordResetView(SuccessMessageMixin,PasswordResetView):
    template_name = 'user/password_reset.html'
    email_template_name = 'user/password_reset_email.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        user=User.objects.filter(email__iexact=request.POST.get('email'))
        if user:
            return super().post(request, *args, **kwargs)
        else:
            return render(request, 'user/password_reset.html',context={"message":"User does not exist"})
