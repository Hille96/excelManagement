# Generated by Django 3.0.7 on 2020-06-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelmanagementApp', '0008_auto_20200619_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='splitexceldata',
            name='Q1',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='Q2',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='Q3',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='Q4',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='deadline',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='fbnr',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='onepager',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='planedYear',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='splitexceldata',
            name='projectnumber',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
