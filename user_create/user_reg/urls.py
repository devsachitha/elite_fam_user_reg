from django.urls import path
from . import views
from .views import JoinRequestView

urlpatterns = [
    path('', JoinRequestView.as_view( )),
]
