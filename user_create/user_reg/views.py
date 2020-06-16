from rest_framework import viewsets
from .serializers import JoinRequestSerializer
from .models import JoinRequest


class JoinRequestViewSet(viewsets.ModelViewSet):
    serializer_class = JoinRequestSerializer
    queryset = JoinRequest.objects.all()
