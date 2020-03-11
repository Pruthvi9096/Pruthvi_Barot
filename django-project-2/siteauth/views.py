from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from siteauth.forms import SignUpForm,LoginForm
from django.contrib import messages

def index(request):
	return render(request,'index.html',{})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect(reverse('index'))
	else:
		form = SignUpForm()
	return render(request,'signup.html',{'form':form})


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect(reverse('index'))
		else:
			messages.error(request,'username or password not correct')
			return redirect(reverse('login'))
		
				
	else:
		form = LoginForm()
	return render(request,'registration/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'logout.html')