from django.urls import path
from .views import Page

urlpatterns = [
    path('image_to_ascii/', Page.as_view(), name='Image_to_ascii'),
]