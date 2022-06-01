# Generated by Django 4.0.4 on 2022-06-01 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscription_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='subscription_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='subscription_website',
            new_name='website',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(db_column='subscription_name', max_length=150),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='website',
            field=models.URLField(db_column='subscription_website'),
        ),
    ]