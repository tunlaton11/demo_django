
from django.shortcuts import render, redirect
from database.models import Rating, Member
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "index.html")



def about(request):
    contact = {
                "Name": "Tunlaton Wongchai",
                "Email": "tunlaton11@gmail.com",
                "Tel.": "0640656605"
            }
    return render(request, "about.html", {"contact":contact})


def contact(request):   
    return render(request, "contact.html")


def signup(request):
    return render(request, "register.html")

def log_in(request):
    return render(request, "login.html")

def log_out(request):
    logout(request)
    return redirect('/')


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        messages.info(request,"Username or Password is invalid")
        return redirect('/login')


def register_check(request):
    username = request.POST['username']
    password = request.POST['password']
    comfirm = request.POST['comfirmpassword']
    nickname = request.POST['nickname']
    if password == comfirm:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'This Username is already exist')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, password=password,first_name=nickname)    
            user.save() 
            return render(request, "success.html")

    else:
        messages.info(request, 'Password is not match')
        return redirect('/register')
    
    







