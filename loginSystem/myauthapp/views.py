from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def mainpage(request):
    return render(request,'home.html')

def singup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
    return render(request,'singup.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse('Username or Password is incorrect!!!')
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')