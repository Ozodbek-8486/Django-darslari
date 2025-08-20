from django.shortcuts import render
from django.views import View

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

class RegisterView(View):
    def get(self,request):
        return render (request,'users/register.html')
class LoginView(View):
    def get(self,request):
        return render(request,'users/login.html' )
    
