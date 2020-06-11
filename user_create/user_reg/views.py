from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import JoinRequest


class JoinRequestView(View):
    """User Join request View"""
    join_requests = JoinRequest.objects.all()

    def get(self, request):
        return HttpResponse('First message from view')
