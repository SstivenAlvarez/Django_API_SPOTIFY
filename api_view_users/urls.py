from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersView

router = DefaultRouter()
router.register(r'usuarios', UsersView)

urlpatterns = [
    path('', include(router.urls)),
]
