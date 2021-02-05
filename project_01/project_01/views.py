
from django.shortcuts import render, redirect
from database.models import Rating, Member
from django.contrib import messages


def home(request):    

    return render(request, "index.html")



def about(request):
    return render(request, "about.html")


def contact(request):
    contact = {
                "Name": "Tunlaton Wongchai",
                "Email": "tunlaton11@gmail.com",
                "Tel.": "0640656605"
            }
    return render(request, "contact.html", {"contact":contact})

def rating(request):
    return render(request, "rating.html")

def signup(request):
    return render(request, "register.html")

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    comfirm = request.POST['comfirmpassword']
    nickname = request.POST['nickname']
    if password == comfirm:
        if Member.objects.filter(username=username).exists():
            messages.info(request, 'This Username is already exist')
            return redirect('/register')
        else:
            user = Member(username=username, password=password,nickname=nickname)    
            user.save() 
            return render(request, "success.html")

    else:
        messages.info(request, 'Password is not match')
        return redirect('/register')
    
    


def result(request):
    email = request.POST['email']
    tel = request.POST['tel']
    comment = request.POST['comment']
    rate = request.POST['rate']    
    add = Rating(email=email, tel=tel, comment=comment, rating=rate)    
    add.save()  
    return render(request, "result.html", {
                                            'email': email,
                                            'tel': tel,
                                            'comment': comment,
                                            'rate': rate
                                            })






