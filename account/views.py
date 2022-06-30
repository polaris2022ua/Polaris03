import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

from django.contrib.auth import authenticate, login

from django.views import View
from account.forms import UserCreationForm

from django.shortcuts import render, redirect


class Register(View):
    template_name = 'registration/register.html'

    def get(self, requset):
        context = {
            'form': UserCreationForm()
        }
        return render(requset, self.template_name, context)

    def post(self, request, img_obj=None):
        form = UserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # phone = form.cleaned_data.get('phone')
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, email=email, phone=phone, password=password)
            # img_obj = form.instance
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')

        context = {
            'form': form,
            'img_obj': img_obj
        }
        return render(request, self.template_name, context)


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')
