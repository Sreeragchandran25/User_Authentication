from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request,'home.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('list_emp')
        else:
            return redirect('loginpage')

    return render(request,'log_in.html')

def registerpage(request):
    form = CreateUserForm()
   
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'register.html',context)

@login_required(login_url='loginpage')
def list_emp(request):
    user = User.objects.all()
    return render(request,'employee_list.html',{'User':user})

def Delete(request,pk):

    data = User.objects.get(id=pk)

    if request.method == 'POST':
        data.delete()
        return redirect('list_emp')
    
    context={'data':data}


    return render(request,'delete.html',context)

def Update(request,pk):

    data=User.objects.get(id=pk)
    form=CreateUserForm(instance=data)
    if request.method == 'POST':
        form=CreateUserForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('list_emp')

    context = {'form':form}

    return render(request,'register.html',context)


def logoutPage(request):
    logout(request)
    return redirect('loginpage')
