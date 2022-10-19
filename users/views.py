from rest_framework import permissions, viewsets
from .models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('email',)
    ordering_fields = ("__all__")
