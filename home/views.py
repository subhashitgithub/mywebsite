from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context={
        'variable':"this is homepage"
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def Blog(request):
    return render(request, 'blog.html')    

def contact(request):
    if request.method== 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        print(name, phone, email, content)
        contact = Contact(name=name, phone=phone, email=email,
        content=content)
        
    return render(request, 'contact.html')


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username, pass1, pass2)
        
    if pass1 != pass2:
        messages.error(request, "password do not match")
    else:
        myuser = User.objects.create_user(username, email, pass1)
        
        myuser.save()

        messages.success(request, "Your Account created successful")
    return redirect('/')

 