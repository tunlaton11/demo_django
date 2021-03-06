"""project_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project_01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about/',views.about, name='about'),
    path('contact/', views.contact, name='contact'),    
    path('register/', views.signup, name='register'),
    path('register_success/',views.register_check, name='register_success'),
    path('login/', views.log_in, name='login'),
    path('login_success/', views.login_check, name='login_success'),
    path('logout/', views.log_out, name='logout'),


]
    
