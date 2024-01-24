from django.core.mail import send_mail

class Mailservice:
    def __init__(self,subject,message,from_email,recipient_list):
        self.subject=subject
        self.message=message
        self.from_email=from_email
        self.recipient_list=recipient_list
    def sendmail(self):
        print("Sending mail.....")
        send_mail(self.subject,
                  self.message,
                  self.from_email,
                  self.recipient_list,
                  fail_silently=True)

