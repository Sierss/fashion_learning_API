# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):

	# Se crea respuesta
	response = {"data": "Hi, this is the fashion learning API"}

	# Se envia respuesta
	return JsonResponse(response)
