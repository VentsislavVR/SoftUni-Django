# Generated by Django 4.2.5 on 2023-09-08 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_album_alter_profile_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('pk',)},
        ),
    ]