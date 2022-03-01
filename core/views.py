from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.

class ReactView(APIView):
	
	def get(self, request):
		detail = [ {"Updated On": detail.updated_on}
		for detail in Image.objects.all()]
		return Response(detail)
