# Generated by Django 4.0.4 on 2022-05-30 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
