# Generated by Django 4.2.13 on 2024-05-29 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('staffID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topicID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=800)),
                ('category', models.CharField(max_length=80)),
                ('group_limit', models.PositiveIntegerField()),
                ('cas', models.BooleanField(default=False)),
                ('syd', models.BooleanField(default=False)),
                ('external', models.BooleanField(default=False)),
                ('chem_eng', models.BooleanField(default=False)),
                ('cns_eng', models.BooleanField(default=False)),
                ('eee', models.BooleanField(default=False)),
                ('mech_eng', models.BooleanField(default=False)),
                ('cs', models.BooleanField(default=False)),
                ('cyb_sec', models.BooleanField(default=False)),
                ('data_sc', models.BooleanField(default=False)),
                ('is_ds', models.BooleanField(default=False)),
                ('seng', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj_app.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('supervisors', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='proj_app.supervisor')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='proj_app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('groupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.group')),
                ('topicID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.topic')),
            ],
        ),
    ]
