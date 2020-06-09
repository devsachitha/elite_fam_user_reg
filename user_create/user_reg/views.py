from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_reg(request):
    return HttpResponse('First message from view')