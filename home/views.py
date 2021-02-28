from django.shortcuts import render,redirect
from .models import Message
# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def education(request):
    return render(request,'education.html')

def skills(request):
    return render(request,'skills.html')


def submit(request):
    if request.method=='POST':
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        x=Message(name=name,email=email,message=message)
        try:
            x.save()
        except:
             print(name,email,message)
        return redirect('/')
    else:
        return render(request,'contact.html')