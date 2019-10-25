#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ContactForm




from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.views.decorators.csrf import csrf_protect
#from django import csrf

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")



def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })
	
	
	
	
	
@csrf_protect	
def register(request):
     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/register/success')

     else:
         form = UserCreationForm()
     token = {}
     #token.update(csrf(request))
     token['form'] = form

     return render_to_response('registration/register.html', token)
@csrf_protect
def registration_success(request):
     return render_to_response('registration/success.html')
	 
	 
	 
	 
	 
@csrf_protect	 
def loggedin(request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})