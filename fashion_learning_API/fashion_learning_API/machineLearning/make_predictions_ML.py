# import cv2
import PIL
from PIL import Image

import numpy as np

import keras
from keras.models import load_model

# Function that returns the predictions given an image input

# Parameters:
# image_path: image path for read image

# Outputs
# return a string with the prediction
def make_predictions(image_path):

	# Create labels
	labels_names = ['T-shirt', "Trouser", "Pullover", 

					"Dress", "Coat", "Sandal", 

					"Shirt", "Sneaker", "Bag", 

					"Ankle boot"

					]

	# Load model
	model = load_model('convolutional_NN_fashion_Mnist.h5')

	img = Image.open(image_path)

	# Image resize
	img = img.resize((28,28)).convert('L')
	
	img = np.array(img)

	img = img.reshape(1, 28,28,1).astype("float32")

	# Normalize data
	img = img / 255

	# Make predictions
	predictions = model.predict(img)

	classes_predictions = np.argmax(predictions, axis = 1)

	names_class_predictions = labels_names[classes_predictions[0]]

	return names_class_predictions