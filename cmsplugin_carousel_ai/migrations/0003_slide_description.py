# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_carousel_ai', '0002_add_call_to_action_label_for_slides'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='description',
            field=models.CharField(max_length=380, verbose_name='slide description', blank=True),
        ),
    ]
