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
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks in seconds
            else:
                request.session.set_expiry(0) 
            
            # Set session variables
            request.session['username'] = username
            request.session['user_id'] = user.id
            print(f"User authenticated, redirecting to dashboard... Username: {username}, User ID: {user.id}")
            
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or password')
            print("Authentication failed.")
    
    return render(request, 'myapp/userlogin.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Campaign, Profile  # Assuming you have a Profile model

@login_required
def dashboard(request):
    user = request.user
    
    # Check if the user has a profile and handle cases where no profile exists
    try:
        profile = user.profile  # Assuming a one-to-one relationship between User and Profile
    except Profile.DoesNotExist:
        profile = None

    # If the user has campaigns associated with them, we can fetch them
    campaigns = Campaign.objects.filter(user=user) if profile else []

    # Add more context if necessary (e.g., handle organization-specific logic)
    context = {
        'user': user,
        'profile': profile,
        'campaigns': campaigns
    }

    return render(request, 'myapp/dashboard.html', context)



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





def index(request):
    # Retrieve all campaigns from the database
    campaigns = Campaign.objects.all()

    # Pass the campaigns to the index.html template
    return render(request, 'myapp/index.html', {'campaigns': campaigns})

def service_details(request):
    return render(request, 'myapp/service-details.html')

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')

def starter_page(request):
    return render(request, 'myapp/starter-page.html')

def campaign2(request):
    return render(request, 'myapp/campaign2.html')

from django.shortcuts import render, get_object_or_404
from .models import Campaign

def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    return render(request, 'myapp/campaign_detail.html', {'campaign': campaign})




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




@login_required  
def reset_password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, ("Passwords do not match."))
        elif len(password) < 8:
            messages.error(request, ("Password must be at least 8 characters long."))
        else:
            user = request.user
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, ("Password has been reset successfully."))
            return redirect('index')  # Redirect to a success page or login page

        return render(request, 'reset_password.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    user = request.user
    # Check if the user has a profile
    if not hasattr(user, 'profile'):
        # If the profile doesn't exist, create one
        Profile.objects.create(user=user)

    # Now, fetch the user's profile
    profile = user.profile

    # Pass the profile and user information to the template
    return render(request, 'myapp/profile.html', {'user': user, 'profile': profile})
