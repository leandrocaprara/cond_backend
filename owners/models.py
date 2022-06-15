from django.utils.translation import gettext_lazy as _
from django.db import models

from building.models import Apartment

# Create your models here.

class Owner(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Owner')
        verbose_name_plural = _('Owners')
        ordering = ('-created',)

    def __str__(self):
        return self.name
        