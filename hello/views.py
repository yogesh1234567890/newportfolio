from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from hello.models import Contact
from hello.forms import *


# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        index = Contact()
        index.name = request.POST['name']
        index.email = request.POST['email']
        index.subject = request.POST['subject']
        index.message = request.POST['message']
        index.save()
        subject = "Regarding the interest in hiring me"
        message ="""Thank you for your interest in my profile and your interest in hiring me. I must say i am currently
        involved in lots of works and i am not currently available. I will be contacting you when i am free.
        Thank you"""
        sent_by = "yogeshbhattarai074@gmail.com"
        sent_to = [request.POST['email']]
        send_mail(subject, message, sent_by, sent_to)
        return redirect('/portfolio/')

    return render(request, "index.html")

@login_required
def Photos(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if(form.is_valid()):
            form.save()
            return redirect('/portfolio/')

    else:
        form = PhotoForm()

    return render(request, "form.html", {'form': form})

@login_required
def fronts(request):
    return render(request, 'index.html', {
        'display': Photos.objects.all(), })

def loginPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request,'Username or password is incorrect')
            

    context={}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was successfully created for '+ user)
            return redirect('login')

    context={'form':form}
    return render(request,"register.html", context)
