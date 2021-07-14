from django.contrib import admin
from .models import *
from translations.admin import TranslatableAdmin, TranslationInline

# Register your models here.
admin.site.register(Menu)
admin.site.register(SubMenu)

admin.site.register(SiteInfo)
admin.site.register(MenuLocation)
admin.site.register(Slider)
