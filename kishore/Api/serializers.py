from rest_framework import serializers
from .models import Api_request

class Api_View(serializers.ModelSerializer):
    class Meta:
        model = Api_request
        fields =('name','age')