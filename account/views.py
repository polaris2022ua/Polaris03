from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from account.forms import UserCreationForm


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
            #img_obj = form.instance
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        context = {
                'form': form,
                'img_obj': img_obj
            }
        return render(request, self.template_name, context)



