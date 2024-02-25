# Generated by Django 5.0.2 on 2024-02-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_synopsis_alter_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cape',
            field=models.CharField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='synopsis',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
