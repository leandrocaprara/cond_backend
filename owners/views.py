from django.shortcuts import render
from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.

class OwnerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
    ordering_fields = ("__all__")
