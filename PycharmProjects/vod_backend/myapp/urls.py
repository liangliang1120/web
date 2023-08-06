from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet, VideoViewSet

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

router.register(r'video', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

