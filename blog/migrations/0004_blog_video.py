# Generated by Django 4.2.1 on 2023-05-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.ImageField(blank=True, null=True, upload_to='videos'),
        ),
    ]
