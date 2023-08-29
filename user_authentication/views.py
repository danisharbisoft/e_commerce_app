from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


# Loads Homepage
def homepage(request):
    return render(request, 'user_authentication/homepage.html')


# Loads user_authentication.html
def authentication(request, person):
    request.session['person'] = person
    return render(request, 'user_authentication/user_authentication.html', {
        'person': person
    })


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

    def form_valid(self, form):
        if self.request.session['person'] == 'buyer':
            return HttpResponseRedirect(reverse('buyer:dashboard'))
        elif self.request.session['person'] == 'seller':
            return HttpResponseRedirect(reverse('seller:dashboard'))
