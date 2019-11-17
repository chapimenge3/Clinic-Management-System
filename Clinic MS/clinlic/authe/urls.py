from django.urls import path,include
from django.contrib import admin
from .views import *
app_name = "authe"
urlpatterns = [
    path('', home , name="homepage"),
    path('login', log1 , name ="login"),
    path('logout', log0, name ="logout"),
    path('', include('django.contrib.auth.urls')),
    path('about', about , name="about"),
    path('doctor', doctor , name="doctor"),
    path('services', services, name='services'),
    path('contact', contact , name ="contact"),
    path('elements', elements , name ="elements"),
    path('single_blog', single_blog , name ="single_blog"),
    path('dep', dep , name ="dep"),
    path('blog', blog , name ="blog"),
    path('patientreg', patientreg , name ="patientreg"),
    
    
]
