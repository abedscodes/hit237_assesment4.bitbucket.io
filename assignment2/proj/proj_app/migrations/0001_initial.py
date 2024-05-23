# Generated by Django 4.2.13 on 2024-05-23 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('staffID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topicID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('is_approved', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='theses', to='proj_app.group')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='supervisors',
            field=models.ManyToManyField(to='proj_app.supervisor'),
        ),
    ]
