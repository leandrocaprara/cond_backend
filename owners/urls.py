from rest_framework.routers import SimpleRouter

from .views import OwnerViewSet

app_name = 'owner'

owner_router = SimpleRouter()
owner_router.register(r'owner', OwnerViewSet)
