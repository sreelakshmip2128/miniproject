# from django.shortcuts import render , HttpResponse, redirect
# from django.contrib import messages
from .models import Registers , Organization

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



def user_login(request):
    return render(request, 'myapp/userlogin.html')

def org_login(request):
    return render(request, 'myapp/orglogin.html')


from .models import Registers

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        # Check if the passwords match
        if password != confirmpassword:
            messages.error(request, "Passwords do not match!")
            return render(request, "myapp/userreg.html")

        # Check if the email already exists in the database
        if Registers.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, "myapp/userreg.html")

        # Create a new user
        data = Registers.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # Hash the password before saving
        )
        data.save()

        messages.success(request, "Registration successful!")
        return redirect("userlogin")  # Redirect to the login page

    return render(request, "myapp/userreg.html")

def org_reg(request):
    if request.method == "POST":
        org_name = request.POST.get('org_name')
        org_email = request.POST.get('org_email')
        org_password = request.POST.get('org_password')
        confirm_org_password = request.POST.get('confirm_org_password')

        # Check if passwords match
        if org_password != confirm_org_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "myapp/orgreg.html")

        # Check if the email already exists in the database
        if Organization.objects.filter(org_email=org_email).exists():
            messages.error(request, "Email already exists!")
            return render(request, "myapp/orgreg.html")

        # Create a new organization
        organization = Organization.objects.create(
            org_name=org_name,
            org_email=org_email,
            org_password=make_password(org_password)  # Hash the password before saving
        )
        organization.save()

        messages.success(request, "Organization registration successful!")
        return redirect("orglogin")  # Redirect to the organization login page

    return render(request, "myapp/orgreg.html")


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


