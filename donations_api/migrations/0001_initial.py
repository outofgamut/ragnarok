# Generated by Django 2.1 on 2018-09-08 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=255)),
                ('payer_id', models.CharField(default='', max_length=255)),
                ('payment_system', models.IntegerField(choices=[(1, 'Paypal'), (2, 'Yandex.Money'), (3, 'Unitpay')])),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('execute_url', models.CharField(default='', max_length=255)),
                ('approval_url', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Donation Log',
                'verbose_name_plural': 'Donations Log',
                'db_table': 'cp_donations_log',
            },
        ),
    ]
