from django.urls import path
from . import views
from .views import reset_password
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('userreg/', views.register, name='userreg'),
    path('userlogin/', views.login_view, name='userlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('orglogin/', views.org_login, name='orglogin'),
    path('orgreg/', views.org_reg, name='orgreg'),
    path('orgdashboard/', views.orgdashboard, name='orgdashboard'),
    path('profile/', views.profile, name='profile'),
    path('create_campaign/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:id>/', views.campaign_detail, name='campaign_detail'),
    path('logout/',views.logoutt, name='logout'),
    path('campaign/<int:campaign_id>/verify/', views.verify_campaign, name='verify_campaign'),
    path('delete/<int:campaign_id>/', views.delete_campaign, name='delete_campaign'),
    path('donate/', views.donate, name='donate'),  # Donation page
    path('payment/callback/', views.payment_callback, name='payment_callback'),
    


    path('reset_password/', reset_password, name='reset_password'),
    path('campaign2/', views.campaign2, name='campaign2'),
    path('service-details/', views.service_details, name='service_details'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    path('starter-page/', views.starter_page, name='starter_page'),
    path('password_reset_info/', views.ForgotPasswordView.as_view(), name='password_reset_info'),
    path('password_reset_infoo/', views.ForgotPasswordView.as_view(), name='password_reset_infoo'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)