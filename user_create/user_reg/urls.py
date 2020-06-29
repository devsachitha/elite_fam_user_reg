from django.urls import path, include
from . import views
from rest_framework import routers
from .views.join_request_viewset import JoinRequestViewSet

router = routers.DefaultRouter()
router.register('join_request', JoinRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
