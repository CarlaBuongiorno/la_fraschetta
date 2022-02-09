from django.urls import path
from . import views


urlpatterns = [
    path('', views.our_story, name='our_story')
]
