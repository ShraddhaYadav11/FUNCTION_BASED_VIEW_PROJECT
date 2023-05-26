
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentLogin
from .models import User
# Create your views here.

def home(request):
    if request.method=='POST':
        fm=StudentLogin(request.POST)
        if fm.is_valid():
         nm=fm.cleaned_data['name']
         em=fm.cleaned_data['email']
         pw=fm.cleaned_data['password']
        
         
         
        
         reg=User(name=nm,email=em,password=pw)
         reg.save()
         fm=StudentLogin()
    else:
        fm=StudentLogin()
    return render(request, 'enroll/home.html',{'form':fm})

def add_Page(request):
    return render(request, 'enroll/add.html')

def show_Page(request):
    stud=User.objects.all()
    return render(request, 'enroll/show.html',{'stu':stud})

def delete_info(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_info(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentLogin(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentLogin(instance=pi)
    return render(request, 'enroll/update.html',{'form':fm})

       