# Generated by Django 4.0.4 on 2022-06-01 03:49

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_rename_subscription_name_subscription_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='renewal_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='renewal_amount_currency',
            new_name='amount_currency',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='amount',
            field=djmoney.models.fields.MoneyField(db_column='renewal_amount', decimal_places=2, default_currency='USD', max_digits=19),
        ),
    ]