# Generated by Django 2.0.5 on 2018-07-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxservice', '0005_auto_20180703_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='oder',
            field=models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='订单号'),
        ),
    ]