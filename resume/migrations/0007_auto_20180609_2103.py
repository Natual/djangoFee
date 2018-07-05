# Generated by Django 2.0.5 on 2018-06-09 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20180609_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='居住地'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='application',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='应聘职位'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='applyCompany',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='应聘公司'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='applyTime',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='申请时间'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='birth',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='degree',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='income',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='目前年收入'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='match',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='匹配程度'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='resident',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='户籍'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='resumeID',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='简历ID'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='self_evaluation',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='自我评价'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='求职状态'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='projectExprience',
            field=models.TextField(blank=True, null=True, verbose_name='项目经验'),
        ),
        migrations.AlterField(
            model_name='wantjob',
            name='address',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='期望工作地点'),
        ),
        migrations.AlterField(
            model_name='wantjob',
            name='busi',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='期望行业'),
        ),
        migrations.AlterField(
            model_name='wantjob',
            name='expectSalary',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='期望薪资'),
        ),
        migrations.AlterField(
            model_name='wantjob',
            name='joinTime',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='到岗时间'),
        ),
        migrations.AlterField(
            model_name='wantjob',
            name='position',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='求职岗位'),
        ),
        migrations.AlterField(
            model_name='wantjob',
            name='workType',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='工作类型'),
        ),
    ]
