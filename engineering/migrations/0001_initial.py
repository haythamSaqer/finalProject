# Generated by Django 4.0.4 on 2022-05-11 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=50)),
                ('creationTime', models.FloatField()),
                ('modificationTime', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MoodBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MoodBoardPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=200)),
                ('moodBoardParent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.moodboard')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StyleMoodBoardPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('styleType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfWindows', models.IntegerField()),
                ('projectIssueDate', models.DateField()),
                ('projectDueDate', models.DateField()),
                ('municipalConfirmed', models.BooleanField()),
                ('customerFinishingConfirm', models.BooleanField(default=False)),
                ('customerNotes', models.TextField()),
                ('currentProgress', models.FloatField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.contract')),
                ('customer', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('projectType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.projecttype')),
            ],
        ),
        migrations.CreateModel(
            name='MoodBoardPartImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images')),
                ('imageNote', models.CharField(max_length=200)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='engineering.moodboardpart')),
            ],
        ),
        migrations.AddField(
            model_name='moodboardpart',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.stylemoodboardpart'),
        ),
        migrations.AddField(
            model_name='moodboardpart',
            name='tableItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.itemstable'),
        ),
        migrations.AddField(
            model_name='moodboard',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.project'),
        ),
        migrations.AddField(
            model_name='moodboard',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engineering.designtype'),
        ),
    ]