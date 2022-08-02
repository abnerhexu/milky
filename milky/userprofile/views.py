from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return redirect("post:postlist")
            else:
                return HttpResponse("Wrong username or password!")
        else:
            return HttpResponse("Invalid username or password!")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("Data should be required in forms of GET or POST")

def user_logout(request):
    logout(request)
    return redirect("post:postlist")