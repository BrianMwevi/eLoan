from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Accounts

# Create your views here.
@login_required(login_url='Login')
def account(request):
    accounts = Accounts.objects.get()
    return render(request, 'accounts.html',accounts)