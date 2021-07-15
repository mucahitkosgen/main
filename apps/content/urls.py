from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

from apps.content.views import (AnnouncementDetailView, AnnouncementListView,
                                NewsCastListView, NewsCastDetailView, OurTeamListView, OurTeamDetailView, SSSListView,
                                ActivityListView, ActivityDetailView, AlbumListView, AlbumDetailView, user_agreement,
                                privacy_policy, SliderDetailView, communication, kvkk,
                                )

app_name = "content"
urlpatterns = [

    #path('', include(('deneyap.urls', 'deneyap'), namespace='deneyap')),
]
