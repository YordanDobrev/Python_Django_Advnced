# Generated by Django 5.1.1 on 2024-10-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_artpainting_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpainting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='macrame',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
