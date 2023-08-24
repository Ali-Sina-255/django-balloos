from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def register_user(request):
    return render(request, 'accounts/register_user.html')


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
