from django.contrib import admin

from translations.admin import TranslatableAdmin, TranslationInline

from apps.parameter.models import TimeCounter, ValueCounter, ValueCounterBox,   \
    AnnouncementSection
#
# admin.site.register(TimeCounter)
# admin.site.register(ValueCounter)
# admin.site.register(ValueCounterBox)
#
# admin.site.register(AnnouncementSection)

