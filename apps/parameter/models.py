import datetime
import json

from ckeditor_uploader.fields import RichTextUploadingField
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from ..common.oneTextField.oneField import OneTextField
from ..common.mixins.audit import AuditMixin
from ..common.fileUpload.userPath import userDirectoryPath
from ..common.fileUpload.validate import validateFileExtension
from django.contrib.auth.models import Group, User
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from translations.models import Translatable
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.timezone import utc
from apps.content.models import Announcement
# Time Counter
class TimeCounter(OneTextField):
    summary = models.CharField(max_length=200, blank=True, verbose_name=_('özet'))
    time_counter = models.DateTimeField()
    bg_image = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                 verbose_name=_('Arkaplan Görsel'))
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('İcon Görsel'))

    @property
    def bg_image_url(self):
        if self.bg_image and hasattr(self.bg_image, 'url'):
            return self.bg_image.url

    @property
    def icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url

    @property
    def time_counter_diff(self):
        # TODO : js ile yapılacak ,bitmedi
        now_2 = timezone.now()
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        now_3 = datetime.datetime.now()
        counter = 0
        print("self.time_counter.year", self.time_counter.year)
        print("self.time_counter.day", self.time_counter.day)
        print("self.time_counter.hour", self.time_counter.hour)
        print("self.time_counter.min", self.time_counter.min)
        print("self.time_counter.second", self.time_counter.second)

        print("self.time_counter :", self.time_counter)
        print("now :", now)
        if self.time_counter > now_2:
            diff = self.time_counter - now_2
            print("diff :", diff)
            print("diff :", diff.days)
            print("diff :", diff.min)
            print("diff :", diff.seconds)
            days, seconds = diff.days, diff.seconds
            hours = days * 24 + seconds // 3600
            hours_2 = diff.total_seconds() / 3600
            hours_3 = hours % 24
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            print("counter diff :", days, hours, hours_2, hours_3, minutes, seconds)
            counter = {"days": days, "hours": hours_3, "minutes": minutes, "seconds": seconds}


        else:
            counter = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

        return counter

    class Meta:
        verbose_name = _('Zaman Sayaç')
        verbose_name_plural = _('Zaman Sayaç')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# Value Counter
class ValueCounter(OneTextField):
    summary = models.CharField(max_length=200, blank=True, verbose_name=_('Özet'))
    counter_box = models.ManyToManyField("ValueCounterBox", verbose_name=_('Sayaç Değerleri'))
    bg_image = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                 verbose_name=_('Arkaplan Görsel'))
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('İcon Görsel'))

    @property
    def bg_image_url(self):
        if self.bg_image and hasattr(self.bg_image, 'url'):
            return self.bg_image.url

    @property
    def icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url

    class Meta:
        verbose_name = _('Değer Sayaç Section')
        verbose_name_plural = _('Değer Sayaç Section')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# Value Counter Box
class ValueCounterBox(OneTextField):
    counter = models.CharField(max_length=200, blank=True, verbose_name=_('Sayaç Değeri'))  # integar veya charfield
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('İcon Görsel'))  # image veya charfield (icon class tag )

    @property
    def icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url

    class Meta:
        verbose_name = _('Değer Sayaç')
        verbose_name_plural = _('Değer Sayaç')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class AnnouncementSection(OneTextField):
    summary = models.CharField(max_length=200, blank=True, verbose_name=_('Özet'))
    Announcements = models.ManyToManyField(Announcement, verbose_name=_('Duyurular'))
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('İcon Görsel'))

    @property
    def icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url

    class Meta:
        # ordering = ('date',)
        verbose_name = _('Duyuru Bölümü')
        verbose_name_plural = _('Duyuru Bölümü')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
