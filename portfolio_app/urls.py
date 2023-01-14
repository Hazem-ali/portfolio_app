from django.urls import path, include
# from .views import MemberViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('', MemberViewSet, basename='members-list')



urlpatterns = [
    path('', include(router.urls)),
]
