from django.shortcuts import render

def login(request):
    return render(request,'accounts/login.html')

def sign_up(request):
    return render(request,'accounts/signup.html')