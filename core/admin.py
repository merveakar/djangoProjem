from django.contrib import admin
from .models import *



@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting





@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description',]

    class Meta:
        model = ImageSetting




