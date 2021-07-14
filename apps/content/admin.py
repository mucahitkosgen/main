from django.contrib import admin

# Register your models here.
from apps.content.models import (Announcement, Slider, WebSites, SSS, AnnouncementCategory, NewsCast, NewsCastCategory, Activity, Album, AlbumImage, )


class AlbumImageInline(admin.TabularInline):
    model = AlbumImage
    prepopulated_fields = {'text':('image',)}


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('text',)
    prepopulated_fields = {'slug': ('text',), }
    inlines = [AlbumImageInline]


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('text', 'category',)
    prepopulated_fields = {'slug': ('text',), }


class NewsCastAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('text',), }


# Register your models here.
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    prepopulated_fields = {'slug': ('first_name', 'last_name',), }


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('text',)
    prepopulated_fields = {'slug': ('text',), }



admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(NewsCast, NewsCastAdmin)
admin.site.register(AnnouncementCategory)
admin.site.register(NewsCastCategory)
admin.site.register(Slider)
admin.site.register(WebSites)
admin.site.register(SSS)
# admin.site.register(AlbumImage)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Activity, ActivityAdmin)
