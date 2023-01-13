"""strona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
# from strona.ocenafilmow import views

#nie działa no module named 'strona.ocenafilmow'
# router = routers.DefaultRouter()
# router.register(r'Aktorzy', views.view_actors)
# router.register(r'Rezyserowie', views.view_directors)
# router.register(r'Filmy', views.view_film)
# router.register(r'Oceny', views.view_oceny)


urlpatterns = [
    # path('',include(router.urls)),
    path('',include('ocenafilmow.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
