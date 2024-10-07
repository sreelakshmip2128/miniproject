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

# from django import template
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import redirect, render, get_object_or_404
# from django.template import loader
# from django.urls import reverse
# from django.db.models import Avg, Sum
# from collections import defaultdict
# from datetime import datetime
# import re
# from apps.home.models import Category, Comment, Donation, Project, Image, Project_Report, Rate, Reply, Tag, Comment_Report
# from apps.home.forms import Project_Form, Report_form, Reply_form, Category_form
# from django.forms.utils import ErrorList
# from apps.authentication.models import Register
# NULL={}

# def getUser(request):
#         user = Register.objects.get(id=request.session['user_id'])
#         return user
    
# def index(request):
#     if 'user_id' in request.session:
#         user = getUser(request)
#     else:
#         user = NULL
        
#     highest_rated_projects = Project.objects.annotate(
#        avg_rate=Avg('rate__rate')).order_by('-avg_rate')[:5]
#     last_5_projects = Project.objects.all().order_by('-id')[:5]
#     featured_projects = Project.objects.filter(is_featured=1)[:5]

#     images = []
#     for project in highest_rated_projects:
#         images.append(project.image_set.all().first().images.url)

#     context = {
#         'highest_rated_projects':highest_rated_projects,
#         'latest_5_projects': last_5_projects,
#         'featured_projects': featured_projects,
#         'images': images,
#         'projects_count': len(Project.objects.all()),
#         'donors_count': len(Donation.objects.all()),
#         'reviews_count': len(Rate.objects.all()),
#         'user': user
#     }
    
#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))


# def create_new_project(request):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         my_images = Image.objects.all()
#         if request.method == 'GET':

#             form = Project_Form()
           
            
#             return render(request, "home/create-project.html", context={"form": form, 'images': my_images, "user":user})

#         if request.method == "POST":
#             tag_error=''
                    
#             if "tag" in request.POST or request.POST['newTag']!="":
                
#                 if(request.POST['newTag']!= ''):

#                     newTag=re.sub("\s+","_",request.POST['newTag'].strip())
#                     new_tag=Tag.objects.create(name=newTag).id
#                     request.POST = request.POST.copy()
#                     request.POST.update({
# 	                "tag":new_tag
#                     })
#             else:
#                 tag_error="Please add tag"
            
                    
#             form = Project_Form(request.POST, request.FILES)
#             if tag_error!="":
                
#                form.add_error('tag',tag_error)
               
#             images = request.FILES.getlist('images')
#             if form.is_valid():
#                 project = form.save(commit=False)
#                 project.user = user
#                 project.save()
#                 form.save_m2m()
#                 for image in images:
#                     Image.objects.create(project_id=project.id, images=image)
#                 return redirect('home')
#         else:
#             form = Project_Form()
#         return render(request, "home/create-project.html", context={"form": form, "user":user})


# def show_project_details(request, project_id):
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)
#     try:
#         project = Project.objects.get(id=project_id)
#         donate = project.donation_set.all().aggregate(Sum("donation"))
#         donations_count = len(project.donation_set.all())
#         comments = project.comment_set.all()
#         replies = Reply.objects.all()
#         project_images = project.image_set.all()
#         counter=[]
#         for image in project_images:
#             counter.append("1")
#         counter.pop()
#         tags = project.tag.all()
#         related_projects_tags = []
#         for tag in tags:
#             related_projects_tags.append(tag.project_set.all())

#         related_projects = Project.objects.none().union(*related_projects_tags)[:4]
#         related_projects_images = []
#         for related_project in related_projects:
#             related_projects_images.append(related_project.image_set.all().first().images.url)


#         myFormat = "%Y-%m-%d %H:%M:%S"
#         today = datetime.strptime(datetime.now().strftime(myFormat), myFormat)
#         end_date = datetime.strptime(project.end_time.strftime(myFormat), myFormat)
#         days_diff = (end_date-today).days
        
#         new_report_form = Report_form()
#         reply = Reply_form()

#         donation_average = (donate["donation__sum"] if donate["donation__sum"] else 0)*100/project.total_target
#         average_rating = project.rate_set.all().aggregate(Avg('rate'))['rate__avg']

        # return user rating if found
#         user_rating = 0
        
#         if 'user_id' in request.session:
    
#             prev_rating=[]

#             if prev_rating:
#                 user_rating = prev_rating[0].rate

#         if average_rating is None:
#             average_rating = 0

#         context = {
#             'project': project,
#             'donation': donate["donation__sum"] if donate["donation__sum"] else 0,
#             'donations': donations_count,
#             'days': days_diff,
#             'comments': comments,
#             'project_images': project_images,
#             'replies': replies,
#             'tags': tags,

#             'report_form': new_report_form,
#             'reply_form': reply,
#             'related_projects': related_projects,
#             'images': related_projects_images,
            
#             'check_target': project.total_target*.25,
#             'donation_average': donation_average,

#             'rating': average_rating*20,
#             'user_rating': user_rating,
#             'rating_range': range(5, 0, -1),
#             'average_rating': average_rating,
            
#             'user':user,
#             'counter':counter
#             }

#         return render(request, "home/project-details.html", context)
#     except Project.DoesNotExist:
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))
 

# def get_tag_projects(request, tag_id):
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)
#     context = {}
#     try:
#         tag = Tag.objects.get(id=tag_id)
#         projects = tag.project_set.all()

#         donations = []
#         progress_values = []
#         images = []
#         for project in projects:
#             donate = project.donation_set.all().aggregate(Sum("donation"))
#             total_donation = donate["donation__sum"] if donate["donation__sum"] else 0
            
#             progress_values.append(total_donation * 100/project.total_target)
#             donations.append(total_donation)
#             images.append(project.image_set.all().first().images.url)

#         context = {
#             'title': tag,
#             'projects': projects,
#             'images': images,
#             'donations': donations,
#             'progress_values': progress_values,
#             'user':user
#         }
#         return render(request, "home/tag-projects.html", context)
#     except Project.DoesNotExist:
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))


# def get_category_projects(request, category_id):
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)
#     context = {}
#     try:
#         projects = Project.objects.filter(
#             category_id=category_id).all()

#         donations = []
#         progress_values = []
#         images = []
#         for project in projects:
#             donate = project.donation_set.all().aggregate(Sum("donation"))
#             total_donation = donate["donation__sum"] if donate["donation__sum"] else 0
#             progress_values.append(total_donation * 100/project.total_target)

#             donations.append(total_donation)

#             images.append(project.image_set.all().first().images.url)

#         title = Category.objects.get(id=category_id)
#         context = {
#             'title': title,
#             'projects': projects,
#             'donations': donations,
#             'images': images,
#             'progress_values': progress_values,
#             'user':user
#         }
#         return render(request, "home/category.html", context)
#     except Project.DoesNotExist:
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))


# def all_projects(request):
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)
#     context = {}
#     try:
#         projects = Project.objects.all()

#         donations = []
#         progress_values = []
#         images = []
#         for project in projects:
#             donate = project.donation_set.all().aggregate(Sum("donation"))
#             total_donation = donate["donation__sum"] if donate["donation__sum"] else 0
#             progress_values.append(total_donation * 100/project.total_target)
#             donations.append(total_donation)
#             images.append(project.image_set.all().first().images.url)

#         context = {
#             'projects': projects,
#             'images': images,
#             'title': 'All Projects',
#             'donations': donations,
#             'progress_values': progress_values,
#             'user':user
#         }
#         return render(request, "home/all_projects.html", context)
#     except Project.DoesNotExist:
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))


# def get_featured_projects(request):
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)
#     context = {}
#     try:
#         projects = Project.objects.filter(is_featured=1).all()

#         donations = []
#         progress_values = []
#         images = []
#         for project in projects:
#             donate = project.donation_set.all().aggregate(Sum("donation"))
#             total_donation = donate["donation__sum"] if donate["donation__sum"] else 0
#             progress_values.append(total_donation * 100/project.total_target)
#             donations.append(total_donation)
#             images.append(project.image_set.all().first().images.url)

#         context = {
#             'projects': projects,
#             'images': images,
#             'title': 'Featured Projects',
#             'donations': donations,
#             'progress_values': progress_values,
#             'user':user
#         }
#         return render(request, "home/all_projects.html", context)
#     except Project.DoesNotExist:
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))


# def donate(request, project_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         if request.method == "POST":
#             if request.POST['donate']:
#                 donation = Donation.objects.create(
#                     donation=request.POST['donate'],
#                     project_id=project_id,
#                     user_id=user.id,
#                 )
#                 return redirect('show_project', project_id)
#         return render(request, "home/project-details.html", project_id , context={"user":user})


# def create_comment(request, project_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         if request.method == "POST":
#             if request.POST['comment']:
#                 comment = Comment.objects.create(
#                     comment=request.POST['comment'],
#                     project_id=project_id,
#                     user_id=user.id
#                 )
#                 return redirect('show_project', project_id)
#         return render(request, "home/project-details.html", project_id , context={"user":user})


# def add_report(request, project_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         my_project = Project.objects.get(id=project_id)
#         if request.method == "POST":
#             Project_Report.objects.create(
#                 report='ip',
#                 project=my_project,
#                 user_id=user.id
#             )
#             return redirect('show_project', project_id)


# def add_comment_report(request, comment_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         my_comment = Comment.objects.get(id=comment_id)
#         project = Project.objects.all().filter(comment__id=comment_id)[0]

#         if request.method == "POST":
#             Comment_Report.objects.create(
#                 report='ip',
#                 comment=my_comment,
#                 user_id=user.id
#             )
#             return redirect('show_project', project.id)


# def create_comment_reply(request, comment_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         if request.method == "POST":
#             if request.POST['reply']:
#                 project = Project.objects.all().filter(comment__id=comment_id)[0]

#                 reply = Reply.objects.create(
#                     reply=request.POST['reply'],
#                     comment_id=comment_id,
#                     user_id=user.id
#                 )
#                 return redirect('show_project', project.id)
#         return render(request, "home/project-details.html", project.id)


# def add_category(request):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         categories = Category.objects.all()

#         if request.method == 'GET':
#             form = Category_form()
#             return render(request, "home/category_form.html", context={'form': form})
#         if request.method == 'POST':
#             form = Category_form(request.POST)

#             if form.is_valid():
#                 new_category = request.POST['name']
#                 for category in categories:
#                     if category.name == new_category:

#                         error = ' not valid'

#                         return render(request, "home/category_form.html", context={'form': form, 'form_error': error})

#                 form.save()
#                 return redirect('home')


# def search(request):
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)
#     context = {}
#     try:
#         search_post = request.GET.get('search')

#         if len(search_post.strip()) > 0:
#             projects = Project.objects.filter(title__icontains=search_post)
#             searched_tags = Tag.objects.filter(name__icontains=search_post)

#             donations = []
#             progress_values = []
#             images = []
#             for project in projects:
#                 donate = project.donation_set.all().aggregate(Sum("donation"))
#                 total_donation = donate["donation__sum"] if donate["donation__sum"] else 0

#                 progress_values.append(
#                     total_donation * 100/project.total_target)
#                 donations.append(total_donation)
#                 images.append(project.image_set.all().first().images.url)

#             context = {
#                 'projects': projects, 
#                 'tags': searched_tags, 
#                 'images': images,
#                 'donations': donations,
#                 'progress_values': progress_values,
#                 'user':user}

#             if(len(projects) <= 0):
#                 context.update(
#                     {'title': 'No Projects Found for "'+search_post+'"'})
#             if(len(searched_tags) <= 0):
#                 context.update(
#                     {'title_tags': 'No Tags Found for "'+search_post + '"'})

#             return render(request, "home/search-result.html", context)
#         else:
#             return render(request, "home/index.html", context)

#     except Project.DoesNotExist:
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))


# def rate(request, project_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         if request.method == "POST":
#             project = get_object_or_404(Project, pk=project_id)
#             context = {"project": project}

#             rate = request.POST.get('rate', '')

#             if rate and rate.isnumeric():

#                 apply_rating(project, user.id, rate)

#         return redirect('show_project', project_id)


# def apply_rating(project, user, rating):

#     # If User rated the same project before --> change rate value
#     prev_user_rating = project.rate_set.filter(user_id=user)
#     if prev_user_rating:
#         prev_user_rating[0].rate = int(rating)
#         prev_user_rating[0].save()

#     # first time to rate this project
#     else:
#         Rate.objects.create(
#             rate=rating, projcet_id=project.id, user_id=user)


# def cancel_project(request, project_id):
#     if 'user_id' not in request.session:
#         user = NULL
#         return redirect('login')
#     else:
#         user = getUser(request)
#         if request.method == 'POST':
#             project = get_object_or_404(Project, pk=project_id)

#             donate = project.donation_set.all().aggregate(Sum("donation"))
#             donation = donate["donation__sum"] if donate["donation__sum"] else 0
#             total_target = project.total_target
            
#             if donation < total_target*.25:
#                 project.delete()
#                 return redirect("profile")
#             else:
#                 return redirect('show_project', project_id)
                
           

# def pages(request):  
#     if 'user_id' not in request.session:
#         user = NULL
#     else:
#         user = getUser(request)     
#     context = {}
#     try : 
#         load_template = request.path.split('/')[-1]
#         if load_template == 'admin':
#                 return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template
#         context['user'] = user

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:
#             html_template = loader.get_template('home/page-404.html')
#             return HttpResponse(html_template.render(context, request))
    


# def send_password_reset_link(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         if email:
#             try:
#                 user = User.objects.get(email=email)
#                 form = PasswordResetForm({'email': email})
#                 if form.is_valid():
#                     form.save(
#                         request=request,
#                         use_https=True,
#                         email_template_name='password_reset_email.html',
#                     )
#                     messages.success(request, "Password reset link has been sent to your email.")
#                 return redirect(reverse('password_reset_done'))
#             except User.DoesNotExist:
#                 messages.error(request, "No user is registered with this email address.")
#     return redirect(reverse('password_reset'))


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


# def org_reg(request):
#     return render(request, 'myapp/orgreg.html')


# //////////////////

# from .models import Organization

# def organization(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirmpassword = request.POST.get('confirmpassword')

       
#         if password != confirmpassword:
#             messages.error(request, "Passwords do not match!")
#             return render(request, "myapp/userreg.html")

       
#         if Organization.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists!")
#             return render(request, "myapp/orgreg.html")
        
#         user=User.objects.create_user(username=username,password=password)

        
#         data = Organization.objects.create(
#             username=username,
#             email=email,
#             password=make_password(password) , 
#             user=user
#         )
#         data.save()

#         messages.success(request, "Registration successful!")
#         return redirect("orglogin")  
#     return render(request, "myapp/orgreg.html")

# def loginview(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         remember_me = request.POST.get('remember_me')
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)

#             if remember_me:
#                 request.session.set_expiry(1209600)  # 2 weeks in seconds
#             else:
#                 request.session.set_expiry(0) 
            
         
#             request.session['username'] = username
#             request.session['user_id'] = user.id
#             print(f"User authenticated, redirecting to dashboard... Username: {username}, User ID: {user.id}")
            
#             return redirect('organization_dashboard')  
#         else:
#             messages.error(request, 'Invalid username or password')
#             print("Authentication failed.")
    
#     return render(request, 'myapp/orglogin.html')

# @login_required
# def organization_dashboard(request):
#     user = request.user
#     try:
#         profile = user.profile 
#     except Profile.DoesNotExist:
#         profile = None  
#     return render(request, 'myapp/organizaton_dashboard.html', {'user': user, 'profile': profile})

# ///////////////////


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



# views.py
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_http_methods

# @require_http_methods(["GET", "POST"])
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
