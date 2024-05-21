# Generated by Django 5.0.6 on 2024-05-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='album.category'),
        ),
    ]