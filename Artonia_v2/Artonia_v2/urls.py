"""
URL configuration for Artonia_v2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include("Artonia_v2.common.urls")),
                  path('accounts/', include('Artonia_v2.accounts.urls')),
                  path('art/', include('Artonia_v2.art_painting.urls')),
                  path('macrame/', include('Artonia_v2.macrame.urls')),
                  path('workshops/', include('Artonia_v2.workshops.urls')),
                  path('artwork/', include('Artonia_v2.artwork.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
