# Generated by Django 4.2.4 on 2023-08-29 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_employeesprojects_accesscard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesscard',
            name='id',
        ),
        migrations.AlterField(
            model_name='accesscard',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee'),
        ),
    ]