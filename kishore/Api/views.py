from django.shortcuts import render
from rest_framework import generics
from .models import Api_request
from .serializers import Api_View
# from rest_framework.response import Response
# from rest_framework import status

# Create your views here.
class Final_view(generics.CreateAPIView):
    queryset = Api_request.objects.all()
    serializer_class = Api_View

class get_view(generics.ListAPIView):
    queryset = Api_request.objects.all()
    serializer_class = Api_View

# class Delete_view(generics.DestroyAPIView):
#     queryset = Api_request.objects.all()
#     serializer_class = Api_View    
#     lookup_field = 'sno'