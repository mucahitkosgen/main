from django.db import models

from django.utils.translation import gettext_lazy as _

from apps.common.fileUpload.userPath import userDirectoryPath
from apps.common.oneTextField import OneTextField
 


class Announcement(OneTextField):
   
    keywords = models.TextField(null=True,blank=True, verbose_name=_('Etiketler'))
    summary = models.CharField(max_length=200, blank=True, verbose_name=_('Özet'))
    content = models.TextField(blank=True, verbose_name=_('İçerik'))
    # alignment = models.IntegerField(null=True, blank=True, unique=True, verbose_name=_('Sıralama'))
    bg_image = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                    verbose_name=_('Arkaplan Görsel'))
    icon = models.ImageField(upload_to=userDirectoryPath, null=True, blank=True,
                                    verbose_name=_('İcon Görsel'))

    date = models.DateTimeField()

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
