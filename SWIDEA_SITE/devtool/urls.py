from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "devtool"

urlpatterns = [
    path('', views.devtool_list, name='devtool_list'),
    path('<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('create/', views.devtool_create, name='devtool_create'),
    path('update/<int:pk>/', views.devtool_update, name='devtool_update'),
    path('delete/<int:pk>/', views.devtool_delete, name='devtool_delete'),
]