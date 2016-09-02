# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_carousel_ai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='call_to_action_label',
            field=models.CharField(blank=True, max_length=250, verbose_name='call to action label'),
        ),
    ]
