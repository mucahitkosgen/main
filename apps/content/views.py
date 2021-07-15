from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from core import settings
from .models import Announcement, SSS, NewsCast, TeamMember, Activity, Slider, Album, KVKK


class AnnouncementListView(ListView):
    model = Announcement
    paginate_by = 6
    template_name = 'content/announcement.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        announcement = Announcement.objects.filter(is_published=True).order_by('created_at')
        return announcement

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)
        context['similar_calls'] = Announcement.objects.filter(is_published=True)[:5]
        return context


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'content/announcement_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementDetailView, self).get_context_data(**kwargs)
        context['similar_calls'] = Announcement.objects.filter(is_published=True)[:5]
        return context


class SSSListView(ListView):
    model = SSS
    template_name = 'content/sss.html'
    context_object_name = 'ssss'
    queryset = SSS.objects.all().order_by('created_at')






class OurTeamListView(ListView):
    model = TeamMember
    template_name = 'content/member.html'
    context_object_name = 'all_member'

    def get_queryset(self):
        all_member = TeamMember.objects.all()
        return all_member

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OurTeamListView, self).get_context_data(**kwargs)
        context['bd'] = TeamMember.objects.filter(level__level='BD')
        context['bt'] = TeamMember.objects.filter(level__level='BT')
        return context


class OurTeamDetailView(DetailView):
    template_name = 'content/member_detail.html'
    model = TeamMember
    context_object_name = 'member'


class NewsCastListView(ListView):
    model = NewsCast
    template_name = 'content/news_casts.html'
    context_object_name = 'news_casts'
    paginate_by = 6

    def get_queryset(self):
        news_casts = NewsCast.objects.filter(is_published=True).order_by('created_at')
        return news_casts


class NewsCastDetailView(DetailView):
    model = NewsCast
    template_name = 'content/news_cast_detail.html'
    context_object_name = 'news_cast'

    def get_context_data(self, **kwargs):
        context = super(NewsCastDetailView, self).get_context_data(**kwargs)
        context['similar_news_casts'] = NewsCast.objects.filter(is_published=True)[:5]
        return context


class ActivityListView(ListView):
    model = Activity
    template_name = 'content/activities.html'

    def get_queryset(self):
        queryset = Activity.objects.filter(is_published=True).order_by('-created_at')
        return queryset


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'content/activity_detail.html'


class AlbumListView(ListView):
    model = Album
    template_name = 'content/albums.html'

    def get_queryset(self):
        queryset = Album.objects.filter(is_published=True).order_by('-created_at')
        return queryset


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'content/album_detail.html'


class SliderDetailView(DetailView):
    model = Slider
    template_name = 'content/slider_detail.html'
    context_object_name = 'slider'


def privacy_policy(request):
    return render(request, 'content/privacy_policy.html')


def user_agreement(request):
    return render(request, 'content/user_agreement.html')


def communication(request):
    return render(request, 'content/communication.html')


def kvkk(request):
    kvkk = KVKK.objects.last()
    return render(request, 'content/kvkk.html', {'kvkk': kvkk})
