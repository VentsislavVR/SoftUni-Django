# Generated by Django 4.2.4 on 2023-08-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee_email_employee_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]