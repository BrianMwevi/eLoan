# Generated by Django 4.0.5 on 2022-06-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_alter_creditor_credit_given_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='account_number',
            field=models.PositiveBigIntegerField(default=0, editable=False, unique=True),
        ),
    ]
