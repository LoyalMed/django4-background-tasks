# Generated by Django 4.2.6 on 2024-01-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0004_auto_20220202_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtask',
            name='repeat',
            field=models.BigIntegerField(choices=[(2, 'every 2 seconds'), (5, 'every 5 seconds'), (10, 'every 10 seconds'), (30, 'every 30 seconds'), (60, 'every 1 minute'), (180, 'every 3 minutes'), (300, 'every 5 minutes'), (600, 'every 10 minutes'), (3600, 'every hour'), (86400, 'every day'), (604800, 'every week'), (1209600, 'every 2 weeks'), (2419200, 'every 4 weeks'), (0, 'never')], default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='repeat',
            field=models.BigIntegerField(choices=[(2, 'every 2 seconds'), (5, 'every 5 seconds'), (10, 'every 10 seconds'), (30, 'every 30 seconds'), (60, 'every 1 minute'), (180, 'every 3 minutes'), (300, 'every 5 minutes'), (600, 'every 10 minutes'), (3600, 'every hour'), (86400, 'every day'), (604800, 'every week'), (1209600, 'every 2 weeks'), (2419200, 'every 4 weeks'), (0, 'never')], default=0),
        ),
    ]
