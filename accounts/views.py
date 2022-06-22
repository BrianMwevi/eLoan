from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.







# AUTHENTICATION VIEWS
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user= authenticate(request,username=username,password=password)
            if user is not None and user.is_lender:
                login(request,user)
                return redirect('lenderpage')
            elif user is not None and user.is_applicant:
                login(request,user)
                return redirect('home')
            else:
                messages.success(request,('there was an error loggig in, please try again...'))
                return redirect('login')
        else:
            return render (request,'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,('you are logged out'))
    return redirect('login')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form =RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                # login(request, user)
                messages.success(request,('Account created for' + ' ' + username))
                return redirect('login')
        else:
            form =RegisterUserForm()


        return render(request,'authenticate/register.html',{'form':form,})