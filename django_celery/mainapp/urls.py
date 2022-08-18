from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.test, name='test'),
    path('sent/', views.send_email_to_all, name='test'),
    path('send_dy/', views.schedule_mail, name='test'),

]