from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'user created succesfully!'},status = 201)
    return Response(serializer.errors,status=404)
    print(serializer.errors)

def home(request):
    return HttpResponse("welcome!")

@csrf_exempt 
@api_view(['GET'])
def get_all(request):
    data = User.objects.all()
    serializer = UserSerializer(data,many = True)
    return Response(serializer.data)

