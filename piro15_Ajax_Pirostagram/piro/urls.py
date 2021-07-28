from django.urls import path
from . import views

app_name = 'piro'

urlpatterns = [
    path('', view=views.post_list, name='post_list'),
    path('<int:pk>/', view=views.post_detail, name='post_detail'),
    path('create/', view=views.post_create, name='post_create'),
    path('like_ajax/', view=views.like_ajax, name='like_ajax'),
    path('comment_write/', view=views.comment_write, name='comment_write'),
    # path('update/<int:pk>/', view=views.post_update, name='post_update'),
    # path('delete/<int:pk>/', view=views.post_delete, name='post_delete'),
]