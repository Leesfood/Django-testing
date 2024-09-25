from django.contrib import admin
from django.urls import path, include
from blogapp import views  # Correct the import

urlpatterns = [
    path('', views.index, name='index'),
    path('readmore/', views.readmore, name='readmore'),
]

# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
