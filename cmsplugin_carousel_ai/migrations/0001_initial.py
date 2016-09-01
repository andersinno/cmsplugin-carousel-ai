# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_carousel_ai_carousel', serialize=False, parent_link=True, primary_key=True, to='cms.CMSPlugin', auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=160)),
                ('interval', models.FloatField(verbose_name='slide changing time in seconds', default=5.0)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('caption', models.CharField(blank=True, verbose_name='slide caption', max_length=160)),
                ('url', models.URLField(blank=True, verbose_name='link to URL', max_length=250)),
                ('ordering', models.IntegerField(db_index=True, verbose_name='ordering', default=0, help_text='Number which determines the order of slides in carousel. Smallest value first.')),
                ('carousel', models.ForeignKey(related_name='slides', verbose_name='carousel', to='cmsplugin_carousel_ai.Carousel')),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', verbose_name='slide image')),
                ('linked_page', models.ForeignKey(null=True, verbose_name='link to page', help_text='Page link overrides given URL.', blank=True, to='cms.Page')),
            ],
            options={
                'ordering': ('ordering',),
            },
        ),
    ]
