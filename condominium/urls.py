from rest_framework.routers import SimpleRouter

from .views import CondominiumViewSet

app_name = 'condominium'

condominium_router = SimpleRouter()
condominium_router.register(r'condominium', CondominiumViewSet)
