# from django.shortcuts import render , HttpResponse, redirect
# from django.contrib import messages
import razorpay
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
from django.contrib.auth import login
from .forms import UserRegistrationForm, ProfileForm  # Ensure this matches the class names
from django.contrib.auth.decorators import login_required
from .models import Campaign, Profile  # Assuming you have a Profile model
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

import logging
logger = logging.getLogger(__name__)



class ForgotPasswordView(TemplateView):
    template_name = 'myapp/password_reset_info.html'

class ForgotPasswordVieww(TemplateView):
    template_name = 'myapp/password_reset_infoo.html'

def user_login(request):
    return render(request, 'myapp/userlogin.html')

def org_login(request):
    return render(request, 'myapp/orglogin.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Registration successful!")
            login(request, user)
            return redirect("userlogin")

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, "myapp/userreg.html", {'user_form': user_form, 'profile_form': profile_form})

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
<<<<<<< HEAD

    # If the user has campaigns associated with them, we can fetch them
    campaigns = Campaign.objects.filter(user=user) if profile else []

    # Add more context if necessary (e.g., handle organization-specific logic)
    context = {
        'user': user,
        'profile': profile,
        'campaigns': campaigns
    }

    return render(request, 'myapp/dashboard.html', context)
=======

    # If the user has campaigns associated with them, we can fetch them
    campaigns = Campaign.objects.filter(user=user) if profile else []

    # Add more context if necessary (e.g., handle organization-specific logic)
    context = {
        'user': user,
        'profile': profile,
        'campaigns': campaigns
    }

    return render(request, 'myapp/dashboard.html', context)

>>>>>>> origin/main



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
<<<<<<< HEAD
     
        # Retrieve all campaigns to list in the organization dashboard
    campaigns = Campaign.objects.all()  # Modify to filter based on organization, if needed
        
    return render(request, 'myapp/organization_dashboard.html', {'campaigns': campaigns})
    
    # Redirect if the user is not an organization
=======
    return render(request, 'myapp/organization_dashboard.html')


>>>>>>> origin/main



def index(request):
    # Retrieve all campaigns from the database
    campaigns = Campaign.objects.all()
<<<<<<< HEAD
=======

    # Pass the campaigns to the index.html template
    return render(request, 'myapp/index.html', {'campaigns': campaigns})
>>>>>>> origin/main

    # Pass the campaigns to the index.html template
    return render(request, 'myapp/index.html', {'campaigns': campaigns})

from django.shortcuts import render, get_object_or_404
from .models import Campaign

def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    return render(request, 'myapp/campaign_detail.html', {'campaign': campaign})



def campaign_detail(request, id):
    # Retrieve the campaign based on the provided id
    campaign = get_object_or_404(Campaign, id=id)
    
    # Assuming there's a User model related to the Campaign model
    owner = campaign.user  # Adjust this according to your actual field name

    # Pass the campaign and the owner to the template
    return render(request, 'myapp/campaign_detail.html', {
        'campaign': campaign,
        'owner': owner
    })

@login_required
def create_campaign(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        image = request.FILES.get('image')  # Get the uploaded image file from the form

        # Create the Campaign instance with the uploaded image
        Campaign.objects.create(
            title=title,
            description=description,
            goal_amount=goal_amount,
            image=image,  # Save the image file in the database
            user=request.user
        )
        return redirect('dashboard')  # Redirect to the dashboard after creation

    return render(request, 'myapp/create_campaign.html')

def logoutt(request):
    logout(request)
    return redirect('index')



<<<<<<< HEAD
=======

>>>>>>> origin/main
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


import logging

logger = logging.getLogger(__name__)

@login_required
def verify_campaign(request, campaign_id):
    try:
        # Attempt to retrieve the UserProfile
        user_profile = Profile.objects.get(user=request.user)
        
        # Get the campaign object
        campaign = get_object_or_404(Campaign, id=campaign_id)

        # Check if the user is an admin or if they are linked to the campaign
        if request.user.is_staff or (user_profile.is_organization and campaign.organization == user_profile):
            campaign.verified = True
            campaign.save()
            
            logger.info(f"Campaign {campaign.id} verified by {request.user.username}")
            return redirect('campaign_detail', campaign_id=campaign.id)
        else:
            logger.warning(f"Unauthorized verification attempt by {request.user.username} on campaign {campaign.id}.")
            return redirect('orgreg')  # or any other appropriate page

    except Profile.DoesNotExist:
        logger.error(f"UserProfile not found for {request.user.username}.")
        return redirect('orgreg')
    
@login_required
def delete_campaign(request, campaign_id):
    # Get the campaign object or return a 404 if not found
    campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)

    if request.method == 'POST':
        campaign.delete()  # Delete the campaign
        return redirect('dashboard')  # Redirect after deletion

    return render(request, 'myapp/delete_campaign.html', {'campaign': campaign})

@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save user info (including email)
            profile_form.save()  # Save profile info (including email if needed)
            return redirect('profile')  # Redirect after success

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)


def donate(request):
    # Pass Razorpay Key ID to the template
    context = {
        'rzp_test_edrzdb8Gbx5U5M': settings.RAZORPAY_KEY_ID
    }
    return render(request, 'donate.html', context)



@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', '')
        order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')

        # Create a Razorpay client instance
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        try:
            # Verify the signature
            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            client.utility.verify_payment_signature(params_dict)

            # If signature is valid, proceed with your logic
            # Save payment details in the database or process as needed
            # ...

            return render(request, 'payment_success.html')

        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Payment verification failed")

    return HttpResponseBadRequest("Invalid request")


# ///////////////////////////////
def service_details(request):
    return render(request, 'myapp/service-details.html')

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')

def starter_page(request):
    return render(request, 'myapp/starter-page.html')

def campaign2(request):
    return render(request, 'myapp/campaign2.html')

# /////////////////////////////////