# Generated by Django 2.0.5 on 2018-06-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_experience_baseinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='mobile',
            field=models.CharField(max_length=24, verbose_name='手机号码'),
        ),
    ]
