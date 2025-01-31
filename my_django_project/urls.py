from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users_app.urls')),  # Include users_app patterns once
]

urlpatterns += staticfiles_urlpatterns()