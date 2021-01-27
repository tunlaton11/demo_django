
from django.shortcuts import render

def home(request):
    data = {"name" : "tun", "age" : 20, "gender" : "male"}

    return render(request, "index.html",  {"data": data})



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




