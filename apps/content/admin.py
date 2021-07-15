from django.contrib import admin

# Register your models here.
from apps.content.models import (Announcement, Slider, WebSites, SSS, AnnouncementCategory, NewsCast, NewsCastCategory,
                                 Activity, Album, AlbumImage, CustomPage, KVKK, )


class AlbumImageInline(admin.TabularInline):
    model = AlbumImage
    prepopulated_fields = {'text': ('image',)}


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


class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('text',)
    prepopulated_fields = {
        'slug': ('text',),
    }

    def save_model(self, request, obj, form, change):
        obj.menu.view_name = 'content:deneyap:custom_page'
        obj.menu.slug = obj.slug
        obj.menu.save()
        super(CustomPageAdmin, self).save_model(request, obj, form, change)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('text',)
    prepopulated_fields = {'slug': ('text',), }

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(NewsCast, NewsCastAdmin)
admin.site.register(AnnouncementCategory)
admin.site.register(NewsCastCategory)
admin.site.register(Slider,SliderAdmin)
admin.site.register(WebSites)
admin.site.register(SSS)
admin.site.register(CustomPage, CustomPageAdmin)
# admin.site.register(AlbumImage)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(KVKK)
