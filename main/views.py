
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re

def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        #getting user data
        firstname =  request.POST.get("fname")
        lastname =  request.POST.get("lname")
        email =  request.POST.get("email")
        pass1 =  request.POST.get("password")
        pass2= request.POST.get("confirm_password")
        username = firstname + '.' + lastname 

        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(firstname or lastname)>20:
            messages.error(request, "Firstname and Lastname must be under 20 charcters!!")
            return redirect('signup')
        
        regex = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])")
        if not regex.search(pass1):
            messages.error(request,"Password must meet the below conditions.")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('signup')
        
        if pass1 == "":
            messages.error(request, "Password cannot be empty")
            return redirect('signup')
        
        if pass2 == "":
            messages.error(request, "Confirm password cannot be empty")
            return redirect('signup')
        
        
        
        
        #creating user from userdata
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "You are Signed up!")
        return redirect('signin')
    
    return render(request, "authentication/signup.html")


def signin(request):
        if request.method == "POST":
            email = request.POST.get("signin-email")
            pas= request.POST.get("signin-password")
            user = authenticate(request,email = email, password = pas)
            print(pas)

            if user is not None:
                login(request,user)
                fname = user.first_name
                print("logged in")
                return render(request, "authentication/test.html", {'fname': fname})
            else:
                messages.error(request,"Something went wrong.")
                return redirect('home')

        return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('signin')


def reset(request):
    return render(request,"authentication/reset.html")

