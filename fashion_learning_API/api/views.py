# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):

	print(request)
	print(request.POST)
	
	# Get the image
	image = request.POST["image"]


	# Se crea respuesta
	response = {"data": image}

	# Se envia respuesta
	return JsonResponse(response)
