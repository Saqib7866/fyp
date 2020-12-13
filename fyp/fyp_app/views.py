from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
def custom(request):
    if(request.method == 'POST'):
        request_data = JSONParser().parse(request)
        return JsonResponse(request_data, status=status.HTTP_201_CREATED)
        # return HttpResponse('Hello world')
