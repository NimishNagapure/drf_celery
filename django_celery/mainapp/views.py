import json
from black import schedule_formatting
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func,send_email_func
from django_celery_beat.models import CrontabSchedule,IntervalSchedule,CrontabSchedule,PeriodicTask
# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done") 

def send_email_to_all(request):
    send_email_func.delay()
    return HttpResponse("sent")
    

def schedule_mail(request):
    schedule,created = CrontabSchedule.objects.get_or_create(
        hour=19,
        minute=44,
    )
    task = PeriodicTask.objects.create(
        crontab= schedule,
        name='send_email_to_all_task_'+'_25',
        task='mainapp.tasks.send_email_func',)
        # args=json.dumps((2,3)))
    return HttpResponse("Done")