import email
from enum import Flag
import profile
import re
from django.contrib import messages
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from customer.models  import *
from .helper import *
import uuid
from django.contrib.auth.hashers import make_password,check_password

def visitor(request):
    return render(request,'visitor.html')

def forgot_password_page(request):
    return render(request,'forgot_password.html')

def change_password_page(request):
    return render(request,'change_password.html')

def signup(request):
    return render(request,'signup_customer.html')

def login(request):
    return render(request,'Login_customer.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        try:
            hashed_pwd = make_password(password)
            check_password(password,hashed_pwd)
            user1=Signup.objects.filter(Username=username)[0]
            if user1 is not None and check_password:
                if user1.flag==2:
                    return render(request,'visitor.html',{'islogin':'true','user':username})
                if user1.flag==0:
                    return HttpResponse("This is for admin page")
                if user1.flag==1:
                    return HttpResponse("This is for chef page")
        except:
            messages.error(request,'Username or password is incorrect')
            return render(request,'Login_customer.html')
    else:
        return render(request,'Login_customer.html')


def register(request):
    if request.method=="POST":
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']
        Cpassword = request.POST['cpassword']
        Phoneno = request.POST['phoneno']

        try:
            check_cust=Signup.objects.filter(Username=Username)[0]
            messages.error(request,'Username is already taken')
            return render(request,'signup_customer.html',{'cuser':'user1'})
        except:
            if Password!=Cpassword:
                messages.error(request,'Password should be match')
                return render(request,'signup_customer.html',{'cuser':'pass1'})
            if len(Phoneno)!=10:
                messages.error(request,'Mobile number should be in 10 digit')
                return render(request,'signup_customer.html',{'cuser':'phone1'})
            tempobj=Signup(Username=Username,Email=Email,Phone_NO=Phoneno,Password=make_password(Password),flag=2)
            tempobj.save()
            return redirect('/')
    else:
        return redirect('/')


def logout(request):
    return render(request,'visitor.html',{'islogin':'false'})


def Changepassword(request,token):
    context={}
    try:
        profile_obj=Profile.objects.filter(forgot_password_token=token).first()
        # print(profile_obj)
        if request.method=='POST':
            new_password=request.POST.get('password')
            confirm_password=request.POST.get('cpassword')
            user_id=request.POST.get('user_id')

            if user_id is None:
                 messages.success(request, 'No user id found.')
                 return redirect(f'/Changepassword/{token}/')

            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/Changepassword/{token}/')


            user_obj=Signup.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login')
    except: 
        pass


def forgot_password(request):
    try:
        if request.method=='POST':
            username=request.POST('username')
            if not Signup.objects.filter(Username=username).first():
               messages.success(request, 'Not user found with this username.')
               return redirect('/forgot_password/')
            
            obj=Signup.objects.get(Username=username)
            token=str(uuid.uuid4())
            profile_obj=Profile.objects.get(user=obj)
            profile_obj.forget_password_token=token
            profile_obj.save()
            send_forget_password_mail(obj.email,token)
            messages.success(request, 'An email is sent.')
            return redirect('/forgot_password/')
    except Exception as e:
        print(e)
    return render(request,'forgot_password.html')

def forgot_password_page(request):
    return render(request,'forgot_password.html')