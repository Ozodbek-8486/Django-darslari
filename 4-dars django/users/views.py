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
    
def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:  # Faqat admin kirsin
            login(request, user)
            return redirect("landing_page")  # login bo‘lsa home sahifaga yuboradi
        else:
            messages.error(request, "Faqat admin login qilishi mumkin!")
    return render(request, "login.html")