from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from hab.forms import * 
from django.shortcuts import render
from hab.models import *
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.

#main_page view
def main_page(request):
   userr = 'u are authenticated'
   variable = { 'authenticated': userr}
   return render(request,'main_page.html',variable)

from django.conf import settings
from django.contrib.auth import get_user_model
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user=User.objects.create_user(username=username,email=email,password=password)

            if user:
               return HttpResponseRedirect('/register/success/')
            else:
               return HttpResponse('Registration failure')
        else :
           return render(request, 'registration/register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html',{'form':form})


def login_page(request):
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
          username = form.cleaned_data.get('username')
          raw_pass = form.cleaned_data.get('password')
          user = authenticate(username = username, password = raw_pass)
          if user is not None:
            login(request, user) 
            return HttpResponseRedirect("/")
          else :
            return HttpResponse("Invalid Login details, username or password incorrect")
       else :
             return HttpResponse(" fill in all textfield ")
    else:

      form = LoginForm()
      variable = {
          'form':form
      }
      return render(request,"registration/login.html",variable)
          

