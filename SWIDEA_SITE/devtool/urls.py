from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "devtool"

urlpatterns = [
    path('', views.devtool_list, name='devtool_list'),
    # path('devtool/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    # path('devtool/create/', views.devtool_create, name='devtool_create'),
    # path('devtool/update/<int:pk>/', views.devtool_update, name='devtool_update'),
    # path('devtool/delete/<int:pk>/', views.devtool_delete, name='devtool_delete'),
]