from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pwa.urls")),
    re_path(r'', include("app1.urls")),
]
