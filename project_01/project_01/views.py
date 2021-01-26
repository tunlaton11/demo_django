
from django.shortcuts import render

def home(request):
    data = {"name" : "tun", "age" : 20, "gender" : "male"}

    return render(request, "index.html",  {"data": data})



def about(request):    
    return render(request, "main.html")




