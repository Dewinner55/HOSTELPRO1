# from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)

