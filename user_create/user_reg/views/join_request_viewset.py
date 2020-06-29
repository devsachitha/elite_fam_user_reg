from rest_framework import viewsets
from ..serializers.join_request_serializer import JoinRequestSerializer
from ..models.join_request import JoinRequest
from rest_framework.authentication import TokenAuthentication


class JoinRequestViewSet(viewsets.ModelViewSet):
    serializer_class = JoinRequestSerializer
    queryset = JoinRequest.objects.all()
    authentication_classes = (TokenAuthentication,)
