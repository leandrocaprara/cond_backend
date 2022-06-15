from django.utils.translation import gettext_lazy as _
from django.db import models

from condominium.models import Condominium
from building.models import Building

# Create your models here.

class Installation(models.Model):
    condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE, null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    require_maintenance = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Installation')
        verbose_name_plural = _('Installations')
        ordering = ('-created',)

    def __str__(self):
        return self.name
        