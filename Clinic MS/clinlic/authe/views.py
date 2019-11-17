from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUp
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.
def home(request):
   user = request.user.is_authenticated
   try:
      users = request.user
      users = User.objects.get(id = users.id)
      return render (request, 'authe/index.html', context={'user' : user , 'users': users , 'isdr' : users.is_dr})
   except Exception:
      return render (request, 'authe/index.html', context={'user' : user })
@login_required
def patientreg(request):
   return render(request , 'authe/patientreg.html') 
def contact(request):
   user = request.user.is_authenticated
   try:
      users = request.user
      users = User.objects.get(id = users.id)
      return render(request , 'authe/contact.html', context={'user' : user , 'users': users , 'isdr' : users.is_dr})
   except Exception:
      return render(request , 'authe/contact.html', context={'user' : user})
def about(request):
   user = request.user.is_authenticated
   try:
      users = request.user
      users = User.objects.get(id = users.id)
      return render(request ,'authe/about.html', context={'user' : user , 'users': users , 'isdr' : users.is_dr})
   except Exception:
      return render(request , 'authe/about.html', context={'user' : user}) 
def doctor(request):
   user = request.user.is_authenticated
   try:
      users = request.user
      users = User.objects.get(id = users.id)
      return render(request ,'authe/doctor.html', context={'user' : user , 'users': users , 'isdr' : users.is_dr})
   except Exception :
      return render(request , 'authe/doctor.html', context={'user' : user})  
@login_required
def services(request):
   user = request.user.is_authenticated
   try:
      users = request.user
      users = User.objects.get(id = users.id)
      return render(request ,'authe/services.html', context={'user' : user , 'users': users , 'isdr' : users.is_dr})
   except Exception:
      return render(request , 'authe/services.html', context={'user' : user}) 
@login_required
def blog(request):
   user = request.user.is_authenticated
   return render(request , 'authe/blog.html', context={'user' : user})
@login_required
def dep(request):
   user = request.user.is_authenticated
   return render(request , 'authe/dep.html', context={'user' : user})
@login_required
def elements(request):
   user = request.user.is_authenticated
   return render(request , 'authe/elements.html', context={'user' : user})
@login_required
def single_blog(request):
   user = request.user.is_authenticated
   return render(request , 'authe/single_blog.html', context={'user' : user})
@login_required
def log0(request):
   return redirect('logout')
@login_required
def log1(request):
   if request.user.is_authenticated:
      return redirect('authe:homepage')
   else:
      return redirect('login')