# Generated by Django 3.2 on 2021-10-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0010_alter_service_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empexpense',
            name='paid',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=10),
        ),
        migrations.AlterField(
            model_name='income',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Till', 'Till')], default='Cash', max_length=10),
        ),
        migrations.AlterField(
            model_name='income',
            name='status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Paid', max_length=10),
        ),
    ]
