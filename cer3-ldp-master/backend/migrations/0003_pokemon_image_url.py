# Generated by Django 5.0.6 on 2024-06-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image_url',
            field=models.CharField(default='No image', max_length=1000),
            preserve_default=False,
        ),
    ]
