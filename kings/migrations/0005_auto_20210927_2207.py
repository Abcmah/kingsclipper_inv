# Generated by Django 3.2 on 2021-09-27 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0004_alter_empexpense_date_repay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empexpense',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kings.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='contact',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='role',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]