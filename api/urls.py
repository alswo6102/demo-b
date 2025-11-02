from django.urls import path
from .views import ping, echo

urlpatterns = [
    path("ping", ping),
    path("echo", echo),
]
