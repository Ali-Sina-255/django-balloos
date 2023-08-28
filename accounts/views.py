from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User
from .utilis import send_notification_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('register_user')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('register_user')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Your registration was successful')
                return redirect('login')
        else:
            messages.error(request, 'password do not match.')
            return redirect('register_user')
    # if request.method == 'POST':
    #
    #     register_form = UserRegistrationForm(request.POST)
    #     if register_form.is_valid():
    #         register_form.save()
    #         messages.success(request, 'Your registration was successful')
    #         return redirect('login')
    #     else:
    #         print('Invalid registration')
    #         print(register_form.errors)
    # else:
    #     register_form = UserRegistrationForm(request.POST)
    # context = {
    #     'register_form': register_form
    # }
    return render(request, 'accounts/login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Your login  was successfully')

            return redirect('login')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logout now.')
    return redirect('login')


def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exct=email)
            #         send rest email
            mail_subject = 'Reset Your password'
            mail_templates = 'accounts/email/reset_password_email.html'
            send_notification_email(request, user, mail_subject, mail_templates)
            messages.success(request, 'password reset link has been send to your email address')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exists')
            return redirect('forget_password')

    return render(request, 'accounts/forget_password.html')


def reset_validated_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.sessoin['uid'] = uid
        messages.info(request, 'Please Reset Your account.')
        return redirect('reset_password')
    else:
        messages.error(request, 'this link has been expired!')
        return redirect('my_account')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'password reset successful')
            return redirect('login')

        else:
            messages.error(request, 'password do not match')
            return redirect('login')
    return render(request, 'accounts/reset_password.html')


def contact(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        name = request.POST['name']
        email = request.POST['email']
        send_mail(
            'Your reception this email form balloon project company.',
            comment,
            'settings.EMAIL_HOST_USER=',
            [email],
            fail_silently=False
        )
        messages.success(request, 'your email send successful.')
        return redirect('home')
    return render(request, 'accounts/contact.html')


