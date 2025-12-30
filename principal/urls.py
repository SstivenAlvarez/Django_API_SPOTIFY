"""
URL configuration for principal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_view_users.views import UsersView
from api_view_users.spotify_views import SpotifyView

router = DefaultRouter()
router.register(r'usuarios', UsersView, basename='usuarios')
router.register(r'spotify', SpotifyView, basename='spotify')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
