# Generated by Django 5.0.7 on 2024-07-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='Click Above To See Full Blog Post', max_length=255),
        ),
    ]
