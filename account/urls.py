
from django.urls import path, include
from account.views import Register, ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),


    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]