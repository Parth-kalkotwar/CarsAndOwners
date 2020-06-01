from django.urls import path, include
from rest_framework import routers

from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'api/cars', views.CarsViewSet, basename='cars')
router.register(r'api/manufacturer', views.ManufacturerViewSer, basename='manufacturer')

urlpatterns = [
    path('', views.index),
    path(r'', include(router.urls)),
    path(r'api/token', TokenObtainPairView.as_view()),
    path(r'api/refresh/token', TokenRefreshView.as_view()),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))

]