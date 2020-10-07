#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
#from django.http import JsonResponse
from django.http import FileResponse

def index(request):
    
    return FileResponse(open('dummyAPI\\fixtures\\initial_data.json', 'rb')) #JsonResponse(initial_data.json, safe=False) #HttpResponse("Hello, world. You're at the API index.")