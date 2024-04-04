from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


#---------Choosing User---------------
def choose_user_view(request):
    return render(request,'accounts/choose.html')

def choose_login_view(request):
    return render(request,'accounts/login_choose.html')


class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('accounts/registration_success.html')


#----------SIGNUP VIEW---------------
class ClientSignUpView(FormView):
    template_name = 'accounts/client_registration.html'
    form_class = ClientRegistrationForm
    
    def form_valid(self, form):
        
        form.save()
        return redirect(reverse('accounts:clientlogin'))
    
class LawyerSignUpView(FormView):
    template_name = 'accounts/lawyer_registration.html'
    form_class = LawyerRegistrationForm
    
    def form_valid(self, form):
        
        form.save()
        return redirect(reverse('accounts:lawyerlogin'))
    

#-----------HOME VIEW-----------

def lawyer_home_view(request):
    return render(request, 'lawyer/lawyer_home.html')

def client_home_view(request):
    return render(request, 'client/client_home.html')
    
#-------------LOGIN VIEW--------------
class LawyerLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/lawyer_login.html'
    
    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user = authenticate(self.request, email=email, password=password)
        
        if user is not None:
            login(self.request, user)
            return redirect(reverse('accounts:lawyer_home'))
        else:
            form.add_error(None, "Invalid email or password.")
            return self.form_invalid(form)
    

    
class ClientLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/client_login.html'
    
    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user = authenticate(self.request, email=email, password=password)
        
        if user is not None:
            login(self.request, user)
            return redirect(reverse('accounts:client_home'))
        else:
            form.add_error(None, "Invalid email or password.")
            return self.form_invalid(form)
    
    
    
    
    
# class LawyerRegisterView(LoginRequiredMixin, CreateView):
#     template_name= 'accounts/lawyer_registration.html'
#     form_class=  RegistrationFormLawyer
#     success_url= reverse_lazy('/')
    
#     def form_valid(self, form):
#         form.instance.user= self.request.user
#         return super().form_valid(form)







