from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serialziers import CarsSerializers, ManufacturerSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Cars,Manufacturer


def index(request):
    return HttpResponse('<h1>Working...<h1>')


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers
    authentication_classes = [ BasicAuthentication,JWTAuthentication,]
    permission_classes = [IsAuthenticated]


class ManufacturerViewSer(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

