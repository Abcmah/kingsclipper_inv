# Generated by Django 3.2 on 2021-09-24 18:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('descriptions', models.TextField()),
                ('cost', models.FloatField()),
                ('supplier', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(default=0, null=True)),
                ('role', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('payment_mode', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('client_balance', models.FloatField(default=0.0)),
                ('time_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kings.team')),
            ],
        ),
    ]
