# from django.shortcuts import render , HttpResponse, redirect
# from django.contrib import messages
from .models import Registers , Organization , Campaign

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse


def send_password_reset_link(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                form = PasswordResetForm({'email': email})
                if form.is_valid():
                    form.save(
                        request=request,
                        use_https=True,
                        email_template_name='password_reset_email.html',
                    )
                    messages.success(request, "Password reset link has been sent to your email.")
                return redirect(reverse('password_reset_done'))
            except User.DoesNotExist:
                messages.error(request, "No user is registered with this email address.")
    return redirect(reverse('password_reset'))


class ForgotPasswordView(TemplateView):
    template_name = 'myapp/password_reset_info.html'

class ForgotPasswordVieww(TemplateView):
    template_name = 'myapp/password_reset_infoo.html'

    



# def dashboard(request):
#     if request.user.is_authenticated:
#         return render(request,'dashboard.html')
#     else:
#         return redirect('userlogin')




    



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
        
        user=User.objects.create_user(username=username,password=password)

        # Create a new user
        data = Registers.objects.create(
            username=username,
            email=email,
            password=make_password(password) , # Hash the password before saving
            user=user
        )
        data.save()

        messages.success(request, "Registration successful!")
        return redirect("userlogin")  # Redirect to the login page

    return render(request, "myapp/userreg.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Set session variables
            request.session['username'] = username
            request.session['user_id'] = user.id
            print(f"User authenticated, redirecting to dashboard... Username: {username}, User ID: {user.id}")
            
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or password')
            print("Authentication failed.")
    
    return render(request, 'myapp/userlogin.html')

@login_required
def dashboard(request):
     if request.user.is_authenticated:
        return render(request, 'myapp/dashboard.html')
     else:
        return redirect("dashboard")


from .models import Organization

def org_reg(request):
    if request.method == 'POST':
        org_name = request.POST.get('org-name')
        org_email = request.POST.get('email')
        org_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if org_password == confirm_password:
            if Organization.objects.filter(org_name=org_name).exists():
                messages.error(request, 'Organization name already exists')
            elif Organization.objects.filter(org_email=org_email).exists():
                messages.error(request, 'Email already exists')
            else:
                organization = Organization(org_name=org_name, org_email=org_email, org_password=org_password)
                organization.save()
                messages.success(request, 'Organization registration successful')
                return redirect('orglogin')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'myapp/orgreg.html')


def org_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('orgdashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'myapp/orglogin.html')

@login_required
def orgdashboard(request):
    return render(request, 'myapp/organization_dashboard.html')


# def org_reg(request):
#     return render(request, 'myapp/orgreg.html')



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



@login_required
def create_campaign(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')

        # Create the Campaign instance
        Campaign.objects.create(
            title=title,
            description=description,
            goal_amount=goal_amount,
            user=request.user
        )
        return redirect('dashboard')  

    return render(request, 'myapp/create_campaign.html')

def logoutt(request):
    logout(request)
    return redirect('index')

