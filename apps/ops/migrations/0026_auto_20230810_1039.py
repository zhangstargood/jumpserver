# Generated by Django 4.1.10 on 2023-08-10 02:36

import common.db.encoder
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0025_auto_20230413_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhoc',
            name='module',
            field=models.CharField(choices=[('shell', 'Shell'), ('win_shell', 'Powershell'), ('python', 'Python'), ('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('sqlserver', 'SQLServer'), ('raw', 'Raw')], default='shell', max_length=128, verbose_name='Module'),
        ),
        migrations.AlterField(
            model_name='historicaljob',
            name='module',
            field=models.CharField(choices=[('shell', 'Shell'), ('win_shell', 'Powershell'), ('python', 'Python'), ('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('sqlserver', 'SQLServer'), ('raw', 'Raw')], default='shell', max_length=128, null=True, verbose_name='Module'),
        ),
        migrations.AlterField(
            model_name='job',
            name='module',
            field=models.CharField(choices=[('shell', 'Shell'), ('win_shell', 'Powershell'), ('python', 'Python'), ('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('sqlserver', 'SQLServer'), ('raw', 'Raw')], default='shell', max_length=128, null=True, verbose_name='Module'),
        ),
        migrations.AlterField(
            model_name='jobexecution',
            name='result',
            field=models.JSONField(blank=True, encoder=common.db.encoder.ModelJSONFieldEncoder, null=True, verbose_name='Result'),
        ),
        migrations.AlterField(
            model_name='jobexecution',
            name='summary',
            field=models.JSONField(default=dict, encoder=common.db.encoder.ModelJSONFieldEncoder, verbose_name='Summary'),
        ),
    ]
