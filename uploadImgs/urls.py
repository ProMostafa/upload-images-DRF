
from django.urls import path, include
from .views import upload_images

urlpatterns = [
    path('upload/', upload_images.as_view(),name='upload'),
]
