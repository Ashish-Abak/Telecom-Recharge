# Generated by Django 5.0.1 on 2024-01-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rechargeapp', '0006_alter_plan_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
