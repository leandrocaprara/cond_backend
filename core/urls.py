from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView)
from rest_framework import routers

from users.urls import users_router

router = routers.DefaultRouter()
#Users
router.registry.extend(users_router.registry)

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