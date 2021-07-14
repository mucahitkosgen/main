from django.conf import settings
from django.conf.urls.static import static

from django.urls import include
from django.contrib import admin
from django.urls import path

from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

app_name = 'core'
urlpatterns = i18n_patterns(
    path('super/user/', admin.site.urls),

    path('', include('T3Sosyal.urls'), name='main_page'),
    path(_('rosetta/'), include('rosetta.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL,
                                                                            document_root=settings.MEDIA_ROOT)
