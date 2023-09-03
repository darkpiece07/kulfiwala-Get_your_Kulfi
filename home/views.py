from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context = {
                "message": "Please login with correct credentials!"
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')

def signupUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def about(request):
    return render(request, 'about.html', )

def services(request):
    return render(request, 'services.html', )

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name'),
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, 'contact.html')
