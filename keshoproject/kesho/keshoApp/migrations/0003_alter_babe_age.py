# Generated by Django 5.0.3 on 2024-04-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keshoApp', '0002_payment_babe_c_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babe',
            name='age',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
