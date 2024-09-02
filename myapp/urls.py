from django.urls import path
from . import views

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
    
      
    # path('orgreg/', views.org_reg, name='orgreg'),
     path('orgreg/', views.org_reg, name='orgreg'),
# new
    # path('organization/dashboard/', views.organization_dashboard, name='organization_dashboard'),
    # path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    # path('approve/<int:request_id>/', views.approve_request, name='approve_request'),
    # path('reject/<int:request_id>/', views.reject_request, name='reject_request'),
]
