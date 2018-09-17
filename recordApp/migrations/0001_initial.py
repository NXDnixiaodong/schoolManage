# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-17 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '\u73ed\u7ea7',
                'verbose_name_plural': '\u73ed\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '\u5e74\u7ea7',
                'verbose_name_plural': '\u5e74\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '\u4e13\u4e1a',
                'verbose_name_plural': '\u4e13\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('id_num', models.CharField(blank=True, max_length=20, null=True)),
                ('tel_num', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(default='\u5728\u6821\u751f', max_length=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.Clazz')),
            ],
            options={
                'verbose_name': '\u5b66\u751f\u4fe1\u606f',
                'verbose_name_plural': '\u5b66\u751f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.Major')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('tel_num', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=30, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
                ('birth', models.DateField(verbose_name='\u51fa\u751f\u65e5\u671f')),
                ('education', models.CharField(max_length=10, verbose_name='\u5b66\u5386')),
                ('over_school', models.CharField(max_length=20, verbose_name='\u6bd5\u4e1a\u9662\u6821')),
                ('id_num', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7')),
                ('ms', models.BooleanField(default=False, verbose_name='\u5a5a\u59fb\u72b6\u6001')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('leave_date', models.DateField()),
                ('is_delete', models.BooleanField(default=False)),
                ('clazz', models.ManyToManyField(to='recordApp.Clazz')),
                ('subject', models.ManyToManyField(to='recordApp.Subject')),
            ],
            options={
                'verbose_name': '\u6559\u5e08\u4fe1\u606f',
                'verbose_name_plural': '\u6559\u5e08\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='stuinfo',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.Subject'),
        ),
        migrations.AddField(
            model_name='clazz',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.Grade'),
        ),
    ]
