# Generated by Django 5.1.3 on 2024-11-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='is_online',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='meeting_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
