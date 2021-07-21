from django.contrib import admin
from django.urls import path, include
#이미지 업로드를 위해 필요한 것들
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('idea.urls')),
    path('devtool/', include('devtool.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
