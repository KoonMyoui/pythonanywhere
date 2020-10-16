from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(req):
	return render(req, 'myweb/base.html')

def united(req):
	return render(req, 'myweb/united.html')



def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST' :
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Username or Password is incorrect')


            except:
                messages.error(request, 'Username not found')
        context = {}
        return render(request, 'myweb/login.html', context)


def logout(req):
    user_logout(req)
    return redirect('index')

@login_required(login_url='login') #เอาไว้ป้องกันเว็บ เวลารีเฟรชมันจะวิ่งไปหน้า login


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()


                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )

                return redirect('login')

            context = {'form':form}
            return render(request, 'myweb/register.html', context)


def contact(req):
    return render(req,'myweb/contact.html')

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

