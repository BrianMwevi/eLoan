# Generated by Django 4.0.5 on 2022-06-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0018_transaction_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
