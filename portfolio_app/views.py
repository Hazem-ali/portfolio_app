from django.shortcuts import render
from rest_framework import viewsets, generics,views
from rest_framework.response import Response

from .models import (ContactData, About, Service)
from .serializers import (ContactDataSerializer, AboutSerializer, ServiceSerializer)



# class ContactDataViewSet(viewsets.ModelViewSet):
#     queryset = ContactData.objects.all()
#     serializer_class = ContactDataSerializer
    # def retrieve(self, request, *args, **kwargs):
    #     user_pk = kwargs.get('pk')
    #     contact_data = ContactData.objects.get(pk=user_pk)
    #     serializer = ContactDataSerializer(contact_data)
    #     return Response(serializer.data)
    

class ListContactDataAPIView(generics.ListCreateAPIView):
    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer


class ContactDataAPIView(views.APIView):
    

    def get(self, request,user):
        user_pk = self.kwargs['user']
        print(user_pk)
        print(user)
        contact_data = ContactData.objects.get(user=user)
        serializer = ContactDataSerializer(contact_data)
        return Response(serializer.data)



    
