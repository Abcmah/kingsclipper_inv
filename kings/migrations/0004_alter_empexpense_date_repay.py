# Generated by Django 3.2 on 2021-09-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0003_alter_empexpense_date_repay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empexpense',
            name='date_repay',
            field=models.DateField(),
        ),
    ]