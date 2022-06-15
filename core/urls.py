from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView)
from rest_framework import routers

from users.urls import users_router
from condominium.urls import condominium_router
from building.urls import (building_router, floor_router, apartment_router)
from installations.urls import (installation_router)
from owners.urls import (owner_router)

router = routers.DefaultRouter()
#Users
router.registry.extend(users_router.registry)

#Condominium
router.registry.extend(condominium_router.registry)

#Building
router.registry.extend(building_router.registry)
router.registry.extend(floor_router.registry)
router.registry.extend(apartment_router.registry)

#Installation
router.registry.extend(installation_router.registry)

#Owners
router.registry.extend(owner_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    #General routes
    path('', include(router.urls)),

    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Swagger
# OpenAPI 3 documentation with Swagger UI
urlpatterns.append(path('schema/', SpectacularAPIView.as_view(urlconf=urlpatterns), name="schema"))

urlpatterns.append(path('docs/', SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui"))