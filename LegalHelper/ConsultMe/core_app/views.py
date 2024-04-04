from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import *
from .models import *
from .forms import ContactForm

from django.urls import reverse
from django.contrib import messages

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    
# def contact(request):
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank You")
#         else:
#             return render(request, 'snippets/contact.html', {'form':form})
        
#     return render(request, 'snippets/contact.html', {'form':ContactForm})

class Contact(FormView):
    form_class= ContactForm
    template_name='snippets/contact.html'
    success_url='/contactclass/'
    
    def form_valid(self, form):
        if len(form.cleaned_data.get('queries'))>20:
            form.add_error('queries', 'Query Length should be in 20 letters')
            return render(self.request, 'snippets/contact.html',{'form':form})
        form.save()
        response=super().form_valid(form)
        return response
    
    def form_invalid(self, form):
        if len(form.cleaned_data.get('queries'))>20:
            form.add_error('queries', 'Query Length should be in 20 letters')
        response = super().form_invalid(form)
        return response
    