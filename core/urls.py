from django.urls import path, include
from django.http import HttpResponse

def healthz(_):
    return HttpResponse("OK", content_type="text/plain")

urlpatterns = [
    path("healthz", healthz),
    path("", include("api.urls")),
]
