from django.urls import path, include
from .views import (ListContactDataAPIView, ContactDataAPIView,
                    ListAboutAPIView, AboutAPIView, ListServiceAPIView, ServiceAPIView)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('contacts', ContactDataViewSet, basename='members-list')


urlpatterns = [
    path('contacts/', ListContactDataAPIView.as_view(), name='contact-data-list'),
    path('contacts/<int:user>', ContactDataAPIView.as_view(),
         name='contact-data-item'),


    path('about/', ListAboutAPIView.as_view(), name='about-list'),
    path('about/<int:user>', AboutAPIView.as_view(),
         name='about-item'),

    path('services/', ListServiceAPIView.as_view(), name='service-list'),
    path('services/<int:user>', ServiceAPIView.as_view(),
         name='service-item'),
    # path('', include(router.urls)),
]
