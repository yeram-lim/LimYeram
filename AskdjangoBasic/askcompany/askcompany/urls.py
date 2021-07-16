from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
]

if settings.DEBUG: #화면 우측에 디버스 툴바가 생긴다.
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns