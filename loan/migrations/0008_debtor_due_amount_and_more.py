# Generated by Django 4.0.5 on 2022-06-22 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loan', '0007_alter_customeraccount_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='debtor',
            name='due_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customeraccount',
            name='account_number',
            field=models.PositiveBigIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='debtor',
            name='paid_amount',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]