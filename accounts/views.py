from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def user_home(request):
    return render(request, 'home.html')


def user_login(request):
    context = {}
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('../success')
            #return HttpResponseRedirect(reverse('success'))
        else:
            context["error"] = "Provide Valid Credentials"
            return  render(request, "login.html", context)
    else:
        return render(request,'login.html',context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'success.html', context)


def user_logout(request):
    if request.method =='POST':
        logout(request)
        return  HttpResponseRedirect(reverse('user_login'))
#
# def login_view(request):
#     next=request.GET.get('next')
#     form=UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username=form.cleaned_data.get('username')
#         password=form.cleaned_data.get('password')
#         user=authenticate(username=username,password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#     context={
#         'form':form
#     }
#     return  render(request,'account/login.html',context)
#
#
#
# def register_view(request):
#     next=request.GET.get('next')
#     form=UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user=form.save(commit=False)
#         password=form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user=authenticate(username=user.username, password=user.password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#     context={
#         'form':form
#     }
#     return  render(request,'account/signup.html',context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('/')
