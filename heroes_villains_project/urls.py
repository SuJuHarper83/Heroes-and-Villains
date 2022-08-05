"""heroes_villains_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# As a developer, I want to register the SuperType model with the admin site so I can:
# Register a new super user (python manage.py createsuperuser)
# Visit the admin site
# Seed two values (“Hero” and “Villain”) into the “super_type” table

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #admin #PW: Password
    path('api/supers/', include('supers.urls')),
    path('api/super_types/,', include('super_types.urls'))
]
