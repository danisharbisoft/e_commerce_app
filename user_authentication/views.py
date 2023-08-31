from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


# Loads Homepage
def homepage(request):
    return render(request, 'user_authentication/homepage.html')


# Loads user_authentication.html
def authentication(request):
    return render(request, 'user_authentication/user_authentication.html')


# Defining the view for registration
class RegisterForm(FormView):
    template_name = 'user_authentication/registration/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('user_authentication:login'))


# Defining the view for login
class CustomLoginView(LoginView):
    template_name = 'user_authentication/registration/login.html'
