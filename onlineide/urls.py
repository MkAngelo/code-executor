"""URLs"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from onlineide import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
]
