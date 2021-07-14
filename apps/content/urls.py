from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

from apps.content.views import (AnnouncementDetailView, AnnouncementListView,
                                NewsCastListView, NewsCastDetailView, OurTeamListView, OurTeamDetailView, SSSListView,
                                ActivityListView, ActivityDetailView, AlbumListView, AlbumDetailView, user_agreement,
                                privacy_policy, SliderDetailView,
                                )

app_name = "content"
urlpatterns = [
    # path('our-team/', OurTeamListView.as_view(), name='member_list'),
    # path('our-team/<slug:slug>/', OurTeamDetailView.as_view(), name='member_detail'),
    # path('announcement/', AnnouncementListView.as_view(), name='announcement'),
    path('announcement/<slug:slug>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('activities/', ActivityListView.as_view(), name='activities'),
    path('activities/<slug:slug>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('albums/', AlbumListView.as_view(), name='albums'),
    path('albums/<slug:slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('news-cast/', NewsCastListView.as_view(), name='news_casts'),
    path('news-cast/<slug:slug>/', NewsCastDetailView.as_view(), name='news_cast_detail'),
    path('user-agreement/', user_agreement, name='user_agreement'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('slider/<slug:slug>/', SliderDetailView.as_view(), name='slider_detail'),
  #  path('', include(('t3bilimturkiye.urls', 't3bilimturkiye'), namespace='t3bilimturkiye')),
]
