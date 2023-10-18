from django.shortcuts import render
from . forms import UserForm, UserProfileForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def user_signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)

        if (user_form.is_valid() and user_profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            if 'profile_pic' in request.FILES:
                user_profile.profile_pic = request.FILES['profile_pic']
            user_profile.save()

            return HttpResponseRedirect(reverse('app1:login'))   
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    }

    return render(request, 'app1/signup.html', context)


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('app1:profile', kwargs={'username': username}))
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('This account is not exist!')

    else:

        user_login_form = UserLoginForm()
        context = {'user_login_form': user_login_form}

    return render(request, 'app1/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_profile(request, username):

    return render(request, 'app1/profile.html')