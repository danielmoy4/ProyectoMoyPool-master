from django.contrib import admin
from django.urls import path, include
from Aplicacion.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("Aplicacion.urls")),
]