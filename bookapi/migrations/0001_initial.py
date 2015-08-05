# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('book_url', models.URLField()),
                ('cover_url', models.URLField()),
            ],
        ),
    ]
