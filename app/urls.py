from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .forms import *

urlpatterns = [
    path('', views.home, name='home'),

    # path('driverregistration/', views.DriverRegistrationForm.as_view(), name='driverregistration'),

    path('customerregistration/', views.CustomerRegistrationForm.as_view(), name='customerregistration'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

    # path('accounts/driverlogin/', auth_views.LoginView.as_view(template_name='app/driverlogin.html', authentication_form=LoginForm), name='driverlogin'),

    # path('customerlogin/', views.CustomerLogin, name='customerlogin'),
    
    # path('accounts/driverlogin/', auth_views.LoginView.as_view(template_name='app/driverlogin.html', authentication_form=LoginForm), name='driverlogin'),

    # path('driverlogin/', views.DriverLogin, name='driverlogin'),

    # path('logout/', views.Logout, name='logout'),

    path('selectcar/', views.CarSelector, name='selectcar'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/changepassworddone/'), name='changepassword'),

    path('changepassworddone/', auth_views.PasswordChangeView.as_view(template_name='app/changepassworddone.html'), name='changepassworddone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'app/passwordreset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name= 'app/passwordresetdone.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'app/passwordresetconfirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'app/passwordresetcomplete.html'), name='password_reset_complete'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('cprofile/', views.ProfileView.as_view(), name='cprofile'),

    path('booking/', views.booking, name='booking'),

    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'app/password_reset.html', form_class=PasswordResetForm), name='password_reset'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)