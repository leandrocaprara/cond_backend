from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Condominium(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Condominium')
        verbose_name_plural = _('Condominiums')
        ordering = ('-created',)

    def __str__(self):
        return self.name
        