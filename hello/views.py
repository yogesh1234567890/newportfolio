from django.shortcuts import render,redirect
from django.http import HttpResponse
from hello.models import Contact


# Create your views here.
def index(request):
    if request.method=='POST':
        index=Contact()
        index.name=request.POST['name']
        index.email=request.POST['email']
        index.subject=request.POST['subject']
        index.message=request.POST['message']
        index.save()
        return redirect ('/portfolio/')

    return render(request, "index.html")
