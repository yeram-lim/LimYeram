from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'piro'

urlpatterns = [
    path('', view=views.post_list, name='list'),
    path('<int:pk>/', view=views.post_detail, name='post_detail'),
    path('create/', view=views.post_create, name='post_create'),
    path('update/<int:pk>/', view=views.post_update, name='post_update'),
    path('delete/<int:pk>/', view=views.post_delete, name='post_delete'),
    path('comment_ajax/', view=views.comment_ajax, name='comment_ajax'),
    path('like_ajax/', view=views.like_ajax, name='like_ajax'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)