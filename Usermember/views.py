from django.shortcuts import render
from .forms import registerForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,decorators
from django.http import HttpResponse  
from django.contrib.auth.mixins import LoginRequiredMixin 
# Create your views here.
class registerUser(View):
	def get(self,request):
		return render(request, 'Usermember/register.html')
	def post(self,request):
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create_user(username, email, password)
		user.save()
		return HttpResponse('save user success')

class loginUser(View):
	def get(self, request):
		return render(request, 'Usermember/login.html') 
	def post(seft,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None: 
			login(request, user)
			return render(request, 'home/view_trainee.html')
		else:
			return HttpResponse('Tên Đăng Nhập Hoặc Mật Khẩu Không Đúng') 
def logoutUser(request):
	logout(request)
	return HttpResponse('You are free')
