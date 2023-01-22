from rest_framework import serializers
from .models import (ContactData, About, Service)



class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = '__all__'
        
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
