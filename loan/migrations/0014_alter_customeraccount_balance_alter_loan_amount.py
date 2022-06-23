# Generated by Django 4.0.5 on 2022-06-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0013_alter_customeraccount_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loan',
            name='amount',
            field=models.FloatField(),
        ),
    ]
