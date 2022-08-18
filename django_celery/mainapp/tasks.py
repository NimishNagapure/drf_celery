from email import message
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from dj_celery import settings
@shared_task(blind=True)
def test_func():
    #operation
    for i in range(10):
        print(i)
    return "Done"


@shared_task(bind=True)
def send_email_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = 'Testing Celery'
        message = "Hello, this is a test email from celery"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"