import re
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

# @login_required(login_url='login')
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


@login_required
def approve_loan(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        sender = request.user
        amount = request.POST.get('amount')
        Transaction.objects.create(
            sender=sender, receiver=receiver, amount=amount)
