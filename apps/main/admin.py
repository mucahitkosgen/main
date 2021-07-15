from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import *


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('text',)
    readonly_fields = ('slug',)


class CustomSubMenuAdmin(admin.ModelAdmin):
    list_display = ('text',)
    prepopulated_fields = {'slug': ('text',), }
    # inlines = [CustomPageTabularInline]


class MenuForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        link_value = cleaned_data.get('view_name')
        redirect_link_value = cleaned_data.get('redirect_link')
        if link_value and redirect_link_value:
            # self.add_error('redirect_link', _('Url ve Yönlendirme Linki aynı anda kullanılamaz.'), )

            raise ValidationError(
                _('Görsünüm adı ve Yönlendirme Linki aynı anda kullanılamaz.'),
                code='invalid',
            )


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(SiteInfo)
admin.site.register(MenuLocation)
