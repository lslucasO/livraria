# Generated by Django 5.0.2 on 2024-02-25 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_cape_book_edition_book_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
