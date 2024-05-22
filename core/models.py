from django.db import models


class GeneralSetting(models.Model):
    name = models.CharField(
        max_length=254,
        blank=True,
        default='',
    )
    description = models.CharField(
        max_length=254,
        blank=True,
        default='',
    )
    parameter = models.CharField(
        max_length=254,
        blank=True,
        default='',
    )
    status = models.BooleanField(  # Yeni alan eklendi
        default=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

