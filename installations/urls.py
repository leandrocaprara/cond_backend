from rest_framework.routers import SimpleRouter

from .views import InstallationViewSet

app_name = 'installation'

installation_router = SimpleRouter()
installation_router.register(r'installation', InstallationViewSet)
