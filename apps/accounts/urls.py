from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from apps.accounts.views import *



app_name = "accounts"

urlpatterns = [
    path('sigin/', sign_in, name='sign_in'),
]


