
"""baykar URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include
from django.contrib import admin
from django.urls import path

from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

from apps.main.views import *

urlpatterns = i18n_patterns(
    path('super/user/', admin.site.urls),

    path('', main, name='mainPage'),
    path('account', accounts, name='accounts'),

    path('test/', test, name='test'),
    path(_('rosetta/'), include('rosetta.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL,
                                                                            document_root=settings.MEDIA_ROOT)