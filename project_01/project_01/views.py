
from django.shortcuts import render
from database.models import Rating


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





