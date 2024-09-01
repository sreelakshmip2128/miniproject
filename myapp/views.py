# from django.shortcuts import render , HttpResponse, redirect
# from django.contrib import messages
from .models import Registers

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



def user_login(request):
    return render(request, 'myapp/userlogin.html')

def org_login(request):
    return render(request, 'myapp/orglogin.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Get the username from the form
        email = request.POST.get('email')        # Get the email from the form
        password = request.POST.get('password')  # Get the password from the form
        confirmpassword = request.POST.get('confirmpassword')  # Get the confirm password from the form

        # Check if the passwords match
        if password != confirmpassword:
            messages.error(request, "Passwords do not match!")
            return render(request, "myapp/userlogin.html")

        # Optionally, you could check if the email already exists in the database
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, "myapp/userlogin.html")

        # Create a new user
        data = Registers.objects.create(
            username=username, 
            email=email, 
            password=make_password(password)  # Hash the password before saving
        )
        data.save()

        messages.success(request, "Registration successful!")
        return redirect("login")  # Redirect to the login page or any other page after registration

    return render(request, "myapp/userreg.html")


def org_reg(request):
    return render(request, 'myapp/orgreg.html')



def index(request):
    return render(request, 'myapp/index.html')

def service_details(request):
    return render(request, 'myapp/service-details.html')

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')

def starter_page(request):
    return render(request, 'myapp/starter-page.html')

def campaign2(request):
    return render(request, 'myapp/campaign2.html')


