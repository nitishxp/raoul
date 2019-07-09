"""raoul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from raoul.views import index
from raoul.render import CustomRenderer

urlpatterns = [
    path('', index),
    path('order/', include('order.urls')),
    path('worker/', include('worker.urls')),
    path('worker-order/', include('assignment.urls')),
    path(
        'docs/',
        include_docs_urls(title="API Documentation",
                          description="",
                          renderer_classes=[CustomRenderer])),
]
