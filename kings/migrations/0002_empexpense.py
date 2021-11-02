# Generated by Django 3.2 on 2021-09-24 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('paid', models.CharField(max_length=10)),
                ('date_repay', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kings.team')),
            ],
        ),
    ]