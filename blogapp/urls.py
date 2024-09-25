from django.contrib import admin
from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls')),  # Blog app URLs
    path('', views.homepage, name='homepage'),  # Root URL points to homepage
]
