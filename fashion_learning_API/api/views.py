# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fashion_learning_API.machineLearning.make_predictions_ML import make_predictions

# Create your views here.
@csrf_exempt
def index(request):

	# Get the image
	image = request.FILES["image"]

	prediction = make_predictions(image.temporary_file_path)
	
	# Se crea respuesta
	response = {"data": prediction}

	# Se envia respuesta
	return JsonResponse(response)
