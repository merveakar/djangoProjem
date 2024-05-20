# from django.contrib import admin
# from core.views import index
# from django.urls import path
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',index,name='index'),
# ]

from django.urls import path
from .views import index
from .views import contact

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
