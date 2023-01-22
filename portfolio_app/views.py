from django.shortcuts import render
from rest_framework import viewsets, generics, views
from rest_framework.response import Response

from rest_framework import status
from .models import (ContactData, About, Service)
from .serializers import (ContactDataSerializer,
                          AboutSerializer, ServiceSerializer)


# class ContactDataViewSet(viewsets.ModelViewSet):
#     queryset = ContactData.objects.all()
#     serializer_class = ContactDataSerializer
# def retrieve(self, request, *args, **kwargs):
#     user_pk = kwargs.get('pk')
#     contact_data = ContactData.objects.get(pk=user_pk)
#     serializer = ContactDataSerializer(contact_data)
#     return Response(serializer.data)



# class ContactDataAPI(generics.GenericAPIView):
#     queryset = ContactData.objects.all()
#     serializer_class = ContactDataSerializer
#     def get_object(self):
#         user_pk = self.kwargs.get('user')
#         print(user_pk)

#         contact_data = ContactData.objects.get(user=user_pk)
#         serializer = ContactDataSerializer(contact_data)
#         return Response(serializer.data)


class ListContactDataAPIView(generics.ListCreateAPIView):
    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer


class ContactDataAPIView(views.APIView):

    def get(self, request, user):

        contact_data = ContactData.objects.get(user=user)
        serializer = ContactDataSerializer(contact_data)
        return Response(serializer.data)

    def delete(self, request, user):

        contact_data = ContactData.objects.get(user=user)
        contact_data.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)


class ListAboutAPIView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutAPIView(views.APIView):

    def get(self, request, user):

        about_details = About.objects.get(user=user)
        serializer = AboutSerializer(about_details)
        return Response(serializer.data)

    def delete(self, request, user):

        about_details = About.objects.get(user=user)
        about_details.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)


class ListServiceAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceAPIView(views.APIView):

    def get(self, request, user):

        service_details = Service.objects.get(user=user)
        serializer = ServiceSerializer(service_details)
        return Response(serializer.data)

    def delete(self, request, user):

        service_details = Service.objects.get(user=user)
        service_details.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
