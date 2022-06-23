from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from accounts.models import User
import datetime as dt
from django.contrib import messages
from .forms import UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):

    return render(request, 'main/home.html', {})


def lenderpage(request):

    return render(request, 'main/lender.html', {})


def about(request):

    return render(request, 'main/about.html', {})


def faqs(request):

    return render(request, 'main/faqs.html', {})


def profile(request, pk):
    user = User.objects.get(id=pk)

    return render(request, 'main/profile.html', {'user': user, })

@login_required(login_url='login')
def update_profile(request, name):
    user = User.objects.get(name=name)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
     
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            return redirect('profile', user.name)
    else:
        user_form = UpdateUserForm(instance=request.user)
    context = {
        'user_form': user_form,
       
    }
    return render(request, 'main/update_profile.html', context)



