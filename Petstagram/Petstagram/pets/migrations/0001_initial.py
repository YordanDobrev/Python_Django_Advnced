# Generated by Django 5.1.1 on 2024-09-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('personal_photo', models.ImageField(upload_to='')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
            ],
        ),
    ]
