# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from fashion_learning_API.machineLearning.make_predictions_ML import make_predictions

import PIL
from PIL import Image
# import numpy as np
# import keras
# from keras.models import load_model


# Create your views here.
@csrf_exempt
def index(request):

	# Get the image
	image = request.FILES["image"]

	# Do predictions using the ML model
	# prediction = make_predictions(image.temporary_file_path)

	print(image)

	print(image.file)

	print(image.file.name)

	prediction = make_predictions(image.file.name)

	# prediction = make_predictions("image.filename")
	
	# Se crea respuesta
	response = {"data": prediction}

	# Se envia respuesta
	return JsonResponse(response)


# Outputs
# return a string with the prediction
def make_predictions(image_path):

	# # Create labels
	# labels_names = ['T-shirt', "Trouser", "Pullover", 

	# 				"Dress", "Coat", "Sandal", 

	# 				"Shirt", "Sneaker", "Bag", 

	# 				"Ankle boot"

	# 				]

	# # Load model
	# model = load_model('convolutional_NN_fashion_Mnist.h5')

	img = Image.open(image_path)

	# # Image resize
	# img = img.resize((28,28)).convert('L')
	
	# img = np.array(img)

	# img = img.reshape(1, 28,28,1).astype("float32")

	# # Normalize data
	# img = img / 255

	# # Make predictions
	# predictions = model.predict(img)

	# classes_predictions = np.argmax(predictions, axis = 1)

	# names_class_predictions = labels_names[classes_predictions[0]]

	# return names_class_predictions

	response = image_path

	return response