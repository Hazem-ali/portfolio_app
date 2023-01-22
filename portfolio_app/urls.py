from django.urls import path, include
from .views import (ListContactDataAPIView, ContactDataAPIView)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('contacts', ContactDataViewSet, basename='members-list')



urlpatterns = [
    path('contacts/<int:user>', ContactDataAPIView.as_view(), name='contact-data-item'),
    # path('contacts/', ListContactDataAPIView.as_view(), name='contact-data-list'),
    # path('', include(router.urls)),
]
