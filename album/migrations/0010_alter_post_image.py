# Generated by Django 5.0.6 on 2024-05-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0009_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
