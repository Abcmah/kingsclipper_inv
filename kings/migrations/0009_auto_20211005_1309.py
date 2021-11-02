# Generated by Django 3.2 on 2021-10-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0008_alter_expenses_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='working',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='income',
            name='status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=10),
        ),
    ]
