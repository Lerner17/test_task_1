from django.urls import path
from .views import VisionAPIView

urlpatterns = [
    path('vision/', VisionAPIView.as_view())
]
