# Generated by Django 2.0.5 on 2018-07-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxservice', '0004_auto_20180703_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge_oder',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
