from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "idea"

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/create/', views.idea_create, name='idea_create'),
    path('idea/update/<int:pk>/', views.idea_update, name='idea_update'),
    path('idea/delete/<int:pk>/', views.idea_delete, name='idea_delete'),
]