# Generated by Django 3.2 on 2022-02-05 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('ip', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=22)),
                ('email', models.CharField(max_length=320)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.server')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.user')),
            ],
        ),
    ]
