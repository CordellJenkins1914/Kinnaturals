# Generated by Django 2.0.2 on 2018-02-16 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_sale_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='charge_id',
        ),
        migrations.AddField(
            model_name='sale',
            name='address',
            field=models.CharField(default='NULL', max_length=250),
        ),
        migrations.AddField(
            model_name='sale',
            name='city',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='sale',
            name='email',
            field=models.EmailField(default='NULL', max_length=254),
        ),
        migrations.AddField(
            model_name='sale',
            name='full_name',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='sale',
            name='postal_code',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='sale',
            name='state',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
