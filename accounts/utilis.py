from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib import  messages


def send_notification_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Please activate your account.'
    messages = render_to_string('account/email/reset_password.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user)

    })
    to_email = user.email
    mail = EmailMessage(messages, mail_subject, to=[to_email])
    mail.send()

