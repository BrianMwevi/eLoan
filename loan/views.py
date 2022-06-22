from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.

# @login_required(login_url='login')
def home(request):

    return render(request, 'main/home.html', {})

def profile(request):

    return render(request,'main/profile.html',{})