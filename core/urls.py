from django.contrib import admin
from core.views import index
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
]

