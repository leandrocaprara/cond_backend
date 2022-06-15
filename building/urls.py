from rest_framework.routers import SimpleRouter

from .views import *

app_name = 'building'

building_router = SimpleRouter()
building_router.register(r'building', BuildingViewSet)

floor_router = SimpleRouter()
floor_router.register(r'floor', FloorViewSet)

apartment_router = SimpleRouter()
apartment_router.register(r'apartment', ApartmentViewSet)
