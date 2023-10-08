from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, UserProfile, Kulfi, Product
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        kulfis = Kulfi.objects.all()
        context = {
            'kulfis' : kulfis
        }
        if request.method == "POST":
            kulfi = request.POST.get('kulfi')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                # print("before quantiy")
                quantity = cart.get(kulfi)
                # print(kulfi)
                # print(quantity)
                if quantity:
                    # print("before remove")
                    if remove:
                        # print("after remove")
                        if quantity <= 1:
                            cart.pop(kulfi)
                        else: 
                            cart[kulfi] = quantity - 1
                    else:
                        print("before adding")
                        cart[kulfi] = quantity + 1
                else:
                    cart[kulfi] = 1
            else:
                cart = {}
                cart[kulfi] = 1

            request.session['cart'] = cart
        return render(request, 'index.html', context)


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

def profileUser(request):
    username = request.user.username
    if UserProfile.objects.filter(name=username):
        user = UserProfile.objects.filter(name=username).values()[0]
        context = {
                'name': user['name'],
                'email': user['email'],
                'phone': user['phone'],
                'job_profile': user['job_profile'],
                'avatar': user['avatar'],
                'url1': user['url1'],
                'address': user['address']
        }
        return render(request, 'profile.html', context)
    else:
        return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html', )

def services(request):
    return render(request, 'services.html', )

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, 'contact.html')


def updateProfileForm(request):
    username = request.user.username
    if UserProfile.objects.filter(name=username):
        user = UserProfile.objects.filter(name=username).values()[0]
        context = {
                'name': user['name'],
                'email': user['email'],
                'phone': user['phone'],
                'job_profile': user['job_profile'],
                'avatar': user['avatar'],
                'url1': user['url1'],
                'address': user['address']
        }
        return render(request, 'update_profile.html', context)
    return render(request, 'update_profile.html')

def updateProfile(request):
    if request.method == "POST":
        name = request.POST.get('fullName')

        user = UserProfile.objects.filter(name = name)[0]
        # print(user['address'])

        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.job_profile = request.POST.get('job_profile')
        user.avatar = request.POST.get('profile_photo')
        user.url1 = request.POST.get('url')
        user.address = request.POST.get('address')

        user.save()
        messages.success(request, "Profile Updated!")
    return redirect('/profile')

def kulfi(request):
    data1 = request.GET.get('data_param')
    kulfi_type = Kulfi.objects.filter(kulfi_name = data1)[0]
    context = {
        'kulfi_name' : kulfi_type.kulfi_name,
        'desc' : kulfi_type.desc,
        'kulfi_pic' : kulfi_type.kulfi_pic,
        'ingredients' : kulfi_type.ingredients,
        'likes' : kulfi_type.likes,
        'dislike' : kulfi_type.dislike,
    }
    return render(request, 'kulfi.html', context)

def vote(request):
    data1 = request.GET.get('param1')
    data2 = request.GET.get('param2')
    kulfi_type = Kulfi.objects.filter(kulfi_name = data1)[0]
    context = {
        'kulfi_name' : kulfi_type.kulfi_name,
        'desc' : kulfi_type.desc,
        'kulfi_pic' : kulfi_type.kulfi_pic,
        'ingredients' : kulfi_type.ingredients,
        'likes' : kulfi_type.likes,
        'dislike' : kulfi_type.dislike,
    }
    if data2 == 'like':
        context['likes'] += 1
        kulfi_type.likes += 1
        kulfi_type.save()
    elif data2 == 'dislike':
        context['dislike'] += 1
        kulfi_type.dislike += 1
        kulfi_type.save()
    return render(request, 'kulfi.html', context)


def debug(request):
    x = 1
    y = 2
    return HttpResponse("this is a debug response!")
