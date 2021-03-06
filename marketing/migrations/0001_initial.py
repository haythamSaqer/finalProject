# Generated by Django 4.0.4 on 2022-05-11 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentTypeName', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.component')),
            ],
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PriceOfferType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workingScope', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingScopeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workingScopeTypeName', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.workingscope')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingScopeTypeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workingScopeTypeNameItem', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.workingscopetype')),
            ],
        ),
        migrations.CreateModel(
            name='PriceOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=200)),
                ('customerFullName', models.CharField(max_length=200)),
                ('customerAddress', models.CharField(max_length=200)),
                ('customerPhoneNumber', models.CharField(max_length=20)),
                ('statement', models.TextField()),
                ('priceInNumber', models.IntegerField()),
                ('priceInLetters', models.CharField(max_length=200)),
                ('totalArea', models.IntegerField()),
                ('totalTimePeriod', models.IntegerField()),
                ('empID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('priceOfferType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.priceoffertype')),
            ],
        ),
        migrations.CreateModel(
            name='MarketingMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=200)),
                ('notes.txt', models.TextField()),
                ('status', models.CharField(choices=[('C', 'Canceled'), ('D', 'Done'), ('P', 'Pending'), ('S', 'Shifted')], max_length=40)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.meetingtype')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=200)),
                ('priceInNumber', models.IntegerField()),
                ('priceInLetters', models.CharField(max_length=200)),
                ('totalArea', models.IntegerField()),
                ('totalTimePeriod', models.IntegerField()),
                ('GregorianDate', models.DateTimeField(auto_now_add=True)),
                ('ContractCoverLetters', models.TextField()),
                ('workingScope', models.TextField()),
                ('additionalDetails', models.TextField()),
                ('MunicipalConfirmed', models.BooleanField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.component')),
                ('contractType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.contracttype')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentTypeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentTypeItem', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.componenttype')),
            ],
        ),
    ]
