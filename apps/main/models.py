from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from apps.common.fileUpload.userPath import userDirectoryPath
from apps.common.oneTextField import OneTextField
#from .urlpatterns import urls, validate_slug
from apps.content.models import Announcement


class SiteInfo(OneTextField):
    keywords = models.TextField(null=True, verbose_name=_('Etiketler'))
    author = models.CharField(max_length=400, null=True, blank=True, verbose_name=_('Sahip'))
    favicon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                verbose_name=_('Favicon'))
    header_logo = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                    verbose_name=_('Üst Logo'))
    footer_logo = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                    verbose_name=_('Alt Logo'))
    address = RichTextField(null=True, verbose_name=_('Adres'))
    phone_list = RichTextField(null=True, verbose_name=_('Telefonlar'))
    footer_address = models.TextField(null=True, verbose_name=_('Footer Adres'))
    copyright = models.TextField(null=True, verbose_name=_('Telif"'))
    phone = models.CharField(max_length=400, null=True, blank=True, verbose_name=_('Telefon'))
    facebook = models.URLField(null=True, blank=True, verbose_name=_('Facebook'))
    twitter = models.URLField(null=True, blank=True, verbose_name=_('Twitter'))
    instagram = models.URLField(null=True, blank=True, verbose_name=_('Instagram'))
    telegram = models.URLField(null=True, blank=True, verbose_name=_('Telegram'))
    bip = models.URLField(null=True, blank=True, verbose_name=_('Bip'))
    whatsapp = models.URLField(null=True, blank=True, verbose_name=_('Whatsapp'))
    youtube = models.URLField(null=True, blank=True, verbose_name=_('Youtube'))
    linkedin = models.URLField(null=True, blank=True, verbose_name=_('Linkedin'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('Email'))
    site_url = models.URLField(null=True, blank=True, verbose_name=_('Site Url'))
  
    @property
    def favicon_url(self):
        if self.favicon and hasattr(self.favicon, 'url'):
            return self.favicon.url

    @property
    def header_logo_url(self):
        if self.header_logo and hasattr(self.header_logo, 'url'):
            return self.header_logo.url

    @property
    def footer_logo_url(self):
        if self.footer_logo and hasattr(self.footer_logo, 'url'):
            return self.footer_logo.url

    class Meta:
        ordering = ('text',)
        verbose_name = _('Site Bilgileri')
        verbose_name_plural = _('Site Bilgileri')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class MenuLocation(OneTextField):
    class Meta:
        verbose_name = _('Menü Konumu')
        verbose_name_plural = _('Menü Konumu')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


import operator
from itertools import chain


# Menus
class Menu(OneTextField):
    menu_location = models.ForeignKey(MenuLocation, null=True, blank=True, on_delete=models.PROTECT,
                                      related_name='menus',
                                      verbose_name=_("Menü Konumu"))

    view_name = models.CharField(max_length=200, unique=True,
                                 blank=True, null=True, verbose_name="Görünüm Adı")
    alignment = models.IntegerField(null=True, blank=True, unique=True, verbose_name=_('Sıralama'))
    redirect_link = models.URLField(null=True, blank=True, verbose_name=_('Yönlendirme Linki'))

    def menu_list(self):
        sub_menu_list = SubMenu.objects.filter(topMenu=self)
        return sub_menu_list

    class Meta:
        verbose_name = _('Menü')
        verbose_name_plural = _('Menü')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# bu modeli kullanan modeller admin panelinde konfügre edilmelidir
class SubMenu(OneTextField):
    topMenu = models.ForeignKey(Menu, on_delete=models.PROTECT, verbose_name=_("Menü"), related_name='sub_menus')
    view_name = models.CharField(max_length=200, null=True, blank=True,
                                 verbose_name="Görünüm Adı", )
    alignment = models.IntegerField(null=True, validators=[MinValueValidator(0)], blank=True,
                                    verbose_name=_('Sıralama'))
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name="Slug", )

    def get_absolute_url(self):
        return reverse(self.view_name, kwargs={'slug': self.slug})

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Alt Menü')
        verbose_name_plural = _('Alt Menü')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
