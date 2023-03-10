from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Database.models import DatabaseModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages

def home(request):
    plant_details=DatabaseModel.objects.all()
    if request.method=="POST":
        search=request.POST.get('plantname')
        if search!=None:
            plant_details=DatabaseModel.objects.filter(plant_name__icontains=search)
        
    data={
        'plant_details':plant_details,
    }
    return render(request, "home.html", data)

def login(request):
    if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            return redirect("myHome")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("userLogin")
    return render(request, "index.html")

def registration(request):
    if request.method == "POST":
        username=request.POST.get('username')
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        
        if not username.isalnum():
            messages.error(request, "Please enter alphanumeric username")
            return redirect("userReg")
        
        if password != cpassword:
            messages.error(request, "Passwords do not match! Please tryagain")
            return redirect("userReg")
    
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.fullname = fullname
            myuser.phone = phone
            myuser.address = address

            myuser.save()
            messages.success(request, "Account has been successfully created!")
            return redirect("userReg")
        
        except:
            messages.error(request, "The username is already exist! Please try another")
            return redirect("userReg")

    return render(request, "registration.html")