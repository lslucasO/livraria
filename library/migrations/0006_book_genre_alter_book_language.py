# Generated by Django 5.0.2 on 2024-02-25 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.language'),
        ),
    ]
