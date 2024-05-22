from django.db import models


class GeneralSetting(models.Model):
    name = models.CharField(
        max_length=254,
        blank=True,
        default='',
        verbose_name='Name',
        help_text='This is variable of general setting',
    )
    description = models.CharField(
        max_length=254,
        blank=True,
        default='',
        verbose_name='Description'

    )
    parameter = models.CharField(
        max_length=254,
        blank=True,
        default='',
        verbose_name='Parameter'

    )
    status = models.BooleanField(  # Yeni alan eklendi
        default=True,
        verbose_name='Status'

    )
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated Date'

    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created Date'

    )


    def __str__(self):
        return f'GeneralSetting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)
