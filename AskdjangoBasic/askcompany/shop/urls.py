from django.urls import path, register_converter#, re_path
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('articles/<yyyy:year>/', views.archives_year, name='archives_year'),
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    # re_path(r'^(?P<pk>\d+)/$', views.item_detail),
] 