# Generated by Django 4.2.4 on 2023-08-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_employee_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=15, verbose_name='Seniority level'),
        ),
    ]
