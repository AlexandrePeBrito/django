# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from sistemaSec.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('partiu-estagio/dashboard', views.dashboard_partiu_estagio, name='dashboard_partiu_estagio'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
