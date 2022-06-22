import re
from django.shortcuts import render, redirect, reverse
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
def apply_loan(request, user_id):
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST, )
        if form.is_valid():
            loan = form.save(commit=False)
            loan.borrower = request.user
            loan.save()
            return redirect(reverse('apply_loan', args=[user_id]))

    return render(request, 'main/loan.html', {'form': form})


@login_required(login_url='login')
def lenderpage(request):
    approved_loans = Loan.objects.filter(approved=True)
    pending_loans = Loan.objects.filter(approved=False)
    return render(request, 'main/lender.html', {'approved_loans': approved_loans, 'pending_loans': pending_loans})


def about(request):
    return render(request, 'main/about.html', {})


def faqs(request):
    return render(request, 'main/faqs.html', {})


def profile(request, pk):
    user = User.objects.get(id=pk)

    return render(request, 'main/profile.html', {'user': user, })


@ login_required
def approve_loan(request, borrower_id):
    if request.method == 'POST':
        receiver = User.objects.get(id=borrower_id)
        sender = request.user
        loan_id = request.POST.get('loan_id', None)
        amount = request.POST.get('amount').split('.')[0]
        Transaction.objects.create(
            sender=sender, receiver=receiver, amount=int(amount))
        loan = Loan.objects.get(id=loan_id)
        loan.approved = True
        loan.save()
    return redirect(reverse('lenderpage'))
