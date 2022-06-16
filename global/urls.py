# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("sistemaSec.autenticacao.urls")),    # Auth routes - login / register
    path("", include("sistemaSec.estagiario.urls")),
    path("", include("sistemaSec.supervisor.urls")),
    path("", include("sistemaSec.home.urls")),            # UI Kits Html files
]
