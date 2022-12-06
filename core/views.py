from django.shortcuts import render
from rest_framework.views import APIView
    # TODO: Define requests here
from rest_framework.response import Response
from rest_framework import status
from .models import core 
from .serializers import GetTraineeSerializer, CoreSerializer

# Create your views here.


class GetAllTrainee(APIView):



	def get(seft, request):
		list_trainee = core.objects.all()
		mydata = GetTraineeSerializer(list_trainee, many = True)
		return Response(data = mydata.data, status = status.HTTP_200_OK)
	


	def post(self, request):
		mydata = CoreSerializer(data = request.data)
		if not mydata.is_valid():
			return Response('sai du lieu', status = status.HTTP_400_BAD_REQUEST)
		SSN = mydata.data['SSN']
		lastname = mydata.data['lastname']
		firstname = mydata.data['firstname']
		birthday = mydata.data['birthday']
		phone = mydata.data['phone']
		address = mydata.data['address']
		company = mydata.data['company']
		cs = core.objects.create(SSN = SSN, lastname = lastname, firstname = firstname, birthday = birthday, phone = phone, address = address, company = company)
		return Response(data = cs.id, status = status.HTTP_200_OK)