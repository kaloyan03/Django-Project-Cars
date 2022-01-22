from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars_auth.forms import RegisterForm, LoginForm


def cars_logout(request):
    logout(request)
    return redirect('login')


def cars_register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)

        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password1']
            user_form.save()
            user = authenticate(email=email, password=password)

            if user:
                login(request, user=user)
                return redirect('landing page')

    else:
        user_form = RegisterForm()

    context = {
        'user_form': user_form
    }

    return render(request, 'auth/register.html', context)


def cars_login(request):
    if request.method == 'POST':
        user_form = LoginForm(request.POST)

        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user=user)
                return redirect('landing page')

    else:
        user_form = LoginForm()

    context = {
        'user_form': user_form
    }

    return render(request, 'auth/login.html', context)