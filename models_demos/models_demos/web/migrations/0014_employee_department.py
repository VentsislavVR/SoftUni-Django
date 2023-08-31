# Generated by Django 4.2.4 on 2023-08-29 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_department_alter_employee_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.department'),
            preserve_default=False,
        ),
    ]
