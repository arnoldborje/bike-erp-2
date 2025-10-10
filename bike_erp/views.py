from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group  
from django.shortcuts import render, redirect

def home_page(request):
    return redirect("dashboard_page")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard_page")

    return render(request, 'index/login.html')


def logout_page(request):
    logout(request)
    return redirect("login_page")


def register_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        print(email, username, password, confirm_password)

        if password != confirm_password:
            # messages.error(request, "Passwords do not match")
            return render(request, "index/register.html")

        if User.objects.filter(username=username).exists():
            # messages.error(request, "Username already taken")
            return render(request, "index/register.html")
        
        if User.objects.filter(email=email).exists():
            # messages.error(request, "Email already registered")
            return render(request, "users/register.html")


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        
        buyer_group, created = Group.objects.get_or_create(name="Buyer")
        user.groups.add(buyer_group)
        
        print(user)
        # messages.success(request, "Account created successfully, you can now log in.")
        return redirect("login_page")
    return render(request, 'index/register.html')