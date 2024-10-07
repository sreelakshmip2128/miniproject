from django.urls import path
from . import views
from .views import reset_password
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('', views.index, name='index'),
    path('service-details/', views.service_details, name='service_details'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    path('starter-page/', views.starter_page, name='starter_page'),
    path('campaign2/', views.campaign2, name='campaign2'),
    # path('userlogin/', views.user_login, name='userlogin'),
    path('orglogin/', views.org_login, name='orglogin'),
    path('userreg/', views.register, name='userreg'),
    # Dashboard URL
    path('userlogin/', views.login_view, name='userlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('password_reset_info/', views.ForgotPasswordView.as_view(), name='password_reset_info'),
    path('password_reset_infoo/', views.ForgotPasswordView.as_view(), name='password_reset_infoo'),

    path('profile/', views.profile, name='profile'),
    path('campaign/<int:id>/', views.campaign_detail, name='campaign_detail'),

    


    path('reset_password/', reset_password, name='reset_password'),
    
    
      
    
    path('orgreg/', views.org_reg, name='orgreg'),
    path('orglogin/', views.org_login, name='orglogin'),
    path('orgdashboard/', views.orgdashboard, name='orgdashboard'),


    path('create_campaign/', views.create_campaign, name='create_campaign'),

    path('logout/',views.logoutt, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)