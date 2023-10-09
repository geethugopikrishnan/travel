from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['user']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cnfrmpass = request.POST['cnfrmpass']
        if password == cnfrmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email ID already exist")
                return redirect('register')
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            user.save()
            print("user created")
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
            return redirect('index.html')
    return render(request, 'register.html')


