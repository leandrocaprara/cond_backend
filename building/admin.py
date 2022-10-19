from django.contrib import admin

from building.models import Apartment, Building, Floor

admin.site.register(Apartment)
admin.site.register(Building)
admin.site.register(Floor)