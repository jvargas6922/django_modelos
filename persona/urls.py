from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index_persona'),
    path('create/', views.create, name='create_persona'),
]
