# Generated by Django 5.0.7 on 2024-07-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest_url',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]