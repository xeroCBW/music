from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginView(request):

    return render(request,'login.html',locals())



def logoutView(request):
    return redirect('/')


@login_required(login_url='/user/login.html')
def homeView(request):
    return render(request,'home.html',locals())