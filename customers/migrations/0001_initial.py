# Generated by Django 4.0.4 on 2022-04-26 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JopType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='Full Time', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('employeeName', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
                ('IsSuperVisor', models.BooleanField(default=False)),
                ('employeeCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.employeecategory')),
                ('employeeJopType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.joptype')),
                ('employeeUserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('customerPhone', models.CharField(max_length=15, unique=True)),
                ('customerEmail', models.EmailField(max_length=254, unique=True)),
                ('isActive', models.BooleanField(default=True)),
                ('userName', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]