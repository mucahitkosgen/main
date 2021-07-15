# Generated by Django 3.0.8 on 2021-07-15 17:08

import apps.common.fileUpload.userPath
import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('view_name', models.CharField(blank=True, choices=[], max_length=200, null=True, unique=True, verbose_name='Görünüm Adı')),
                ('alignment', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Sıralama')),
                ('redirect_link', models.URLField(blank=True, null=True, verbose_name='Yönlendirme Linki')),
            ],
            options={
                'verbose_name': 'Menü',
                'verbose_name_plural': 'Menü',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MenuLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Menü Konumu',
                'verbose_name_plural': 'Menü Konumu',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('keywords', models.TextField(null=True, verbose_name='Etiketler')),
                ('author', models.CharField(blank=True, max_length=400, null=True, verbose_name='Sahip')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, verbose_name='Favicon')),
                ('header_logo', models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, verbose_name='Üst Logo')),
                ('footer_logo', models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, verbose_name='Alt Logo')),
                ('address', ckeditor.fields.RichTextField(null=True, verbose_name='Adres')),
            ],
            options={
                'verbose_name': 'Site Bilgileri',
                'verbose_name_plural': 'Site Bilgileri',
                'ordering': ('text',),
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('view_name', models.CharField(blank=True, choices=[], max_length=200, null=True, verbose_name='Görünüm Adı')),
                ('alignment', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sıralama')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug')),
                ('topMenu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_menus', to='main.Menu', verbose_name='Menü')),
            ],
            options={
                'verbose_name': 'Alt Menü',
                'verbose_name_plural': 'Alt Menü',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menus', to='main.MenuLocation', verbose_name='Menü Konumu'),
        ),
    ]
