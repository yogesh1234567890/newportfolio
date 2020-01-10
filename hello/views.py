from django.shortcuts import render, redirect
from django.http import HttpResponse
from hello.models import Contact
from hello.forms import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        index = Contact()
        index.name = request.POST['name']
        index.email = request.POST['email']
        index.subject = request.POST['subject']
        index.message = request.POST['message']
        index.save()
        return redirect('/portfolio/')

    return render(request, "index.html")


def photos(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if(form.is_valid()):
            form.save()
            return redirect('/portfolio/')

    else:
        form = PhotoForm()

    return render(request, "form.html", {'form': form})


def fronts(request):
    return render(request,'index.html',{
            'display':Photos.objects.all(), })
