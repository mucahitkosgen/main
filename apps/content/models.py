from datetime import datetime

from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.common.fileUpload.userPath import userDirectoryPath, image_upload_to
from apps.common.oneTextField import OneTextField
from ckeditor.fields import RichTextField


class AnnouncementCategory(OneTextField):
    color = ColorField(max_length=200, verbose_name=_('Renk Kodu'))

    class Meta:
        verbose_name = _('Duyuru Kategorisi')
        verbose_name_plural = _('Duyuru Kategorileri')


class Announcement(OneTextField):
    category = models.ForeignKey(AnnouncementCategory, verbose_name=_('Duyuru Kategorisi', ),
                                 related_name='announcements', on_delete=models.PROTECT)
    keywords = models.TextField(null=True, blank=True, verbose_name=_('Etiketler'))
    summary = models.CharField(max_length=400, blank=True, verbose_name=_('Özet'))
    # alignment = models.IntegerField(null=True, blank=True, unique=True, verbose_name=_('Sıralama'))
    bg_image = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                 verbose_name=_('Arkaplan Görsel'))
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('İcon Görsel'))
    content = RichTextField(blank=True, verbose_name=_('İçerik'))
    is_published = models.BooleanField(default=True)
    date = models.DateTimeField()
    slug = models.SlugField(blank=False, unique=True)

    def get_absolute_url(self):
        return reverse('content:announcement_detail', kwargs={'slug': self.slug})

    @property
    def bg_image_url(self):
        if self.bg_image and hasattr(self.bg_image, 'url'):
            return self.bg_image.url

    @property
    def icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url

    class Meta:
        ordering = ('date',)
        verbose_name = _('Duyuru')
        verbose_name_plural = _('Duyuru')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# Slider todo atolye eklendiğinde slider ekle
class Slider(OneTextField):
    bg_image = models.ImageField(upload_to='slider/images', null=True, blank=True,
                                 verbose_name=_('Görsel'))
    redirect_link = models.URLField(null=True, blank=True, verbose_name=_('Yönlendirme Linki'))

    is_published = models.BooleanField(default=True, verbose_name=_('Yayınlansın mı?'))
    alignment = models.IntegerField(null=True, blank=True, unique=True, verbose_name=_('Sıralama'))
    date = models.DateTimeField()

    @property
    def bg_image_url(self):
        if self.bg_image and hasattr(self.bg_image, 'url'):
            return self.bg_image.url

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Slider')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# context processors
class WebSites(OneTextField):
    logo = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('Logo'))
    site_url = models.URLField(max_length=300, verbose_name=_('Site Url'))
    detail_info = RichTextField(null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Yayına alınsın mı?')

    class Meta:
        verbose_name = _('Web Site')
        verbose_name_plural = _('Web Siteler')

    @property
    def bg_image_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url


class SSS(OneTextField):
    text = models.TextField(null=False, verbose_name=_('Soru'))
    answer = models.TextField(null=False, verbose_name=_('Cevap'))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Sıkça Sorular Soru')
        verbose_name_plural = _('Sıkça Sorular Sorular')


class NewsCastCategory(OneTextField):
    color = ColorField(max_length=200, default='#ffffff', verbose_name=_('Renk Kodu'))

    class Meta:
        verbose_name = _('Haber Kategorisi')
        verbose_name_plural = _('Haber Kategorileri')


class NewsCast(OneTextField):
    category = models.ForeignKey(NewsCastCategory, verbose_name=_('Haber Kategorisi', ),
                                 related_name='news_casts', on_delete=models.PROTECT)
    keywords = models.TextField(null=True, blank=True, verbose_name=_('Etiketler'))
    summary = models.CharField(max_length=400, blank=True, verbose_name=_('Özet'))
    # alignment = models.IntegerField(null=True, blank=True, unique=True, verbose_name=_('Sıralama'))
    bg_image = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                 verbose_name=_('Arkaplan Görsel'))
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                             verbose_name=_('İcon Görsel'))
    content = RichTextField(blank=True, verbose_name=_('İçerik'))
    is_published = models.BooleanField(default=True)
    date = models.DateTimeField()
    slug = models.SlugField(blank=False, unique=True)

    @property
    def bg_image_url(self):
        if self.bg_image and hasattr(self.bg_image, 'url'):
            return self.bg_image.url

    @property
    def icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url

    def get_absolute_url(self):
        return reverse('content:news_cast_detail', kwargs={'slug': self.slug})  # new

    class Meta:
        verbose_name = _('Haber')
        verbose_name_plural = _('Haberler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class MemberLevel(OneTextField):
    LEVEL = (
        ('BD', _('Board of Directors')),
        ('BT', _('Board of Trustees')),
    )
    level = models.CharField(max_length=200, blank=False, choices=LEVEL, verbose_name=_('Ekipteki Konumu'))

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Üyenin Konumu')
        verbose_name_plural = _('Üye Konumları')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


#

class TeamMember(OneTextField):
    first_name = models.CharField(max_length=200, blank=False, verbose_name=_('Adı'))
    last_name = models.CharField(max_length=200, blank=False, verbose_name=_('Soyadı'))
    level = models.ManyToManyField(MemberLevel, max_length=5, related_name='members', blank=False,
                                   verbose_name=_('Ekipteki Konumu'))
    biography = models.TextField(blank=False)
    twitter = models.URLField(null=True, blank=True, verbose_name=_('Twitter'))
    instagram = models.URLField(null=True, blank=True, verbose_name=_('Instagram'))
    linkedin = models.URLField(null=True, blank=True, verbose_name=_('Linkedin'))
    facebook = models.URLField(null=True, blank=True, verbose_name=_('Facebook'))
    email = models.URLField(null=True, blank=True, verbose_name=_('Email'))
    profile_photo = models.ImageField(upload_to='teams/member_photo', blank=False)
    slug = models.SlugField(blank=True, )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('content:member_detail', kwargs={'slug': self.slug})  # new

    def photo(self):
        if self.profile_photo and hasattr(self.profile_photo, 'url'):
            return self.profile_photo.url

    def level_list(self):
        levels = self.level

        list = '/ '.join(level.get_level_display() for level in levels.all())

        return list

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Ekip Üyesi')
        verbose_name_plural = _('Ekip Üyeleri')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Activity(OneTextField):
    creator = models.CharField(max_length=300, blank=False, verbose_name=_('Oluşturan'))
    image = models.ImageField(verbose_name=_('Afiş'))
    summary = models.CharField(max_length=400, blank=True, verbose_name=_('Özet'))
    content = RichTextField(verbose_name=_('Etkinlik İçeriği'))
    date = models.DateTimeField(verbose_name=_('Etkinlik Tarihi'))
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True, verbose_name=_('Yayınlansın mı?'))

    def get_absolute_url(self):
        return reverse('content:activity_detail', kwargs={'slug': self.slug})  # new

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Aktivite')
        verbose_name_plural = _('Aktiviteler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Album(OneTextField):
    date = models.DateTimeField(verbose_name=_('Albüm Tarihi'))
    about = RichTextField(verbose_name=_('Albüm Hakkında'), null=True, blank=True)
    image = models.ImageField(upload_to='albums', verbose_name=_('Albüm Kapağı'), null=True, blank=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True, verbose_name=_('Yayınlansın mı?'))

    def get_absolute_url(self):
        return reverse('content:album_detail', kwargs={'slug': self.slug})

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_images(self):
        images = AlbumImage.objects.filter(album=self)
        return images

    class Meta:
        ordering = ('date',)
        verbose_name = _('Albüm')
        verbose_name_plural = _('Albümler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


def image_upload_to(instance, filename):
    now = datetime.now()
    path = "images/{year}/{month}/{day}/{model}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        model=instance.album.text,
        filename=filename
    )
    return path


class AlbumImage(OneTextField):
    text = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Başlık'))
    album = models.ForeignKey(Album, related_name='images', verbose_name=_('Albüm'), on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.image.name

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Resim')
        verbose_name_plural = _('Resimler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
