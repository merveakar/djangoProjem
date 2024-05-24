from django.db import models

class GeneralSetting(models.Model):
    name = models.CharField('Name', max_length=254, blank=True, default='', help_text='This is the name of the general setting')
    description = models.CharField('Description', max_length=254, blank=True, default='')
    parameter = models.CharField('Parameter', max_length=254, blank=True, default='')
    status = models.BooleanField('Status', default=True)
    updated_date = models.DateTimeField('Updated Date', auto_now=True)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

    def __str__(self):
        return self.name

class ImageSetting(models.Model):
    name = models.CharField('Name', max_length=254, blank=True, default='', help_text='This is the name of the image setting')
    description = models.CharField('Description', max_length=254, blank=True, default='')
    file = models.ImageField('Image', upload_to='images/', blank=True, null=True, help_text='Upload the image for this setting')
    status = models.BooleanField('Status', default=True)
    updated_date = models.DateTimeField('Updated Date', auto_now=True)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

    def __str__(self):
        return self.name
