# Generated by Django 2.0.5 on 2018-06-24 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fee',
            fields=[
                ('payId', models.IntegerField(max_length=8, primary_key=True, serialize=False, verbose_name='费用ID')),
                ('monthlyFee', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='每月缴纳金额')),
                ('feeDone', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='当期已缴纳的金额')),
                ('feeOwn', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='当期仍需交纳的金额')),
                ('month', models.CharField(max_length=8, verbose_name='当期所属的月份')),
                ('payMethod', models.IntegerField(max_length=4, verbose_name='缴纳方式：1=按月缴纳，3=按季度缴纳，12=按年缴纳')),
                ('status', models.IntegerField(max_length=4, verbose_name='当期缴纳状态: 0= 未缴纳完毕，1= 已缴纳完毕')),
                ('createTime', models.DateTimeField(verbose_name='创建时间')),
                ('updateTime', models.DateTimeField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '缴费信息',
                'verbose_name': '缴费信息',
            },
        ),
        migrations.CreateModel(
            name='pay_user',
            fields=[
                ('user_id', models.IntegerField(max_length=8, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('open_id', models.CharField(blank=True, max_length=36, null=True, verbose_name='微信的openid')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=12, verbose_name='手机号码')),
                ('idCard', models.CharField(blank=True, max_length=20, null=True, verbose_name='身份证号码')),
                ('staff', models.CharField(blank=True, max_length=16, null=True, verbose_name='职务职级')),
                ('staffNo', models.CharField(blank=True, max_length=20, null=True, verbose_name='员工编号')),
                ('depart', models.CharField(max_length=100, verbose_name='党支部名称')),
                ('createTime', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '党员信息',
                'verbose_name': '党员信息',
            },
        ),
        migrations.AddField(
            model_name='fee',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wxservice.pay_user', verbose_name='用户ID'),
        ),
    ]
