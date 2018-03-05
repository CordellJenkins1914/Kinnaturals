# Generated by Django 2.0.2 on 2018-02-15 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='order',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='sale', to='orders.Order'),
        ),
    ]
