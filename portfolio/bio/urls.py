from django.urls import path
from bio import views

urlpatterns = [
    path('', views.bio, name='bio'),
]