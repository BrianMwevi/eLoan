from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from accounts.models import User
import datetime as dt
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def home(request):
    return render(request, 'main/home.html', {})

@login_required(login_url='login')
def apply_loan(request,user_id):
    user=User.objects.get(id=user_id)
    user1=request.user
    form=LoanForm(request.POST, )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/loan.html', {'form':form,'user':user})


@login_required(login_url='login')
def deposit(request,user_id):
    user=User.objects.get(id=user_id)
    form=DepositForm(request.POST, )

    return render(request, 'main/deposit.html', {'form':form,'user':user})


@login_required(login_url='login')
def lenderpage(request):
    return render(request, 'main/lender.html', {})


def about(request):
    return render(request, 'main/about.html', {})


def faqs(request):
    return render(request, 'main/faqs.html', {})

@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)

    return render(request, 'main/profile.html', {'user': user, })
