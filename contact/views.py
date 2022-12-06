from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from core.models import core
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class addtrainee(LoginRequiredMixin, View):
	login_url = '/login/'
	def get(self,request):
		return render(request, 'contact/add_trainee.html') 


 
	


def insert(request):
	if request.method == "POST":
		SSN = request.POST['SSN']
		lastname = request.POST['lastname']
		firstname = request.POST['firstname']
		birthday = request.POST['birthday']
		phone = request.POST['phone']
		address = request.POST['address']
		company = request.POST['company']
		my = core(SSN = SSN, lastname = lastname, firstname = firstname, birthday = birthday, phone = phone, address = address, company = company)
		my.save()
		return HttpResponse('success')
	else:
		return HttpResponse('not success')


def login(request):
	return render(request, '/Usermember/')