# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-08-07 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionKnob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minval', models.CharField(max_length=32, null=True, verbose_name='minimum value')),
                ('maxval', models.CharField(max_length=32, null=True, verbose_name='maximum value')),
                ('tunable', models.BooleanField(verbose_name='tunable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='dbmscatalog',
            name='type',
            field=models.IntegerField(choices=[(1, 'MySQL'), (2, 'Postgres'), (3, 'Db2'), (4, 'Oracle'), (6, 'SQLite'), (7, 'HStore'), (8, 'Vector'), (5, 'SQL Server'), (9, 'MyRocks')]),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='default',
            field=models.TextField(verbose_name='default value'),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='enumvals',
            field=models.TextField(null=True, verbose_name='valid values'),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='maxval',
            field=models.CharField(max_length=32, null=True, verbose_name='maximum value'),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='minval',
            field=models.CharField(max_length=32, null=True, verbose_name='minimum value'),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='resource',
            field=models.IntegerField(choices=[(1, 'Memory'), (2, 'CPU'), (3, 'Storage'), (4, 'Other')], default=4),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='summary',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='tunable',
            field=models.BooleanField(verbose_name='tunable'),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='unit',
            field=models.IntegerField(choices=[(1, 'bytes'), (2, 'milliseconds'), (3, 'other')]),
        ),
        migrations.AlterField(
            model_name='knobcatalog',
            name='vartype',
            field=models.IntegerField(choices=[(1, 'STRING'), (2, 'INTEGER'), (3, 'REAL'), (4, 'BOOL'), (5, 'ENUM'), (6, 'TIMESTAMP')], verbose_name='variable type'),
        ),
        migrations.AlterField(
            model_name='metriccatalog',
            name='metric_type',
            field=models.IntegerField(choices=[(1, 'COUNTER'), (2, 'INFO'), (3, 'STATISTICS')]),
        ),
        migrations.AlterField(
            model_name='metriccatalog',
            name='summary',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='metriccatalog',
            name='vartype',
            field=models.IntegerField(choices=[(1, 'STRING'), (2, 'INTEGER'), (3, 'REAL'), (4, 'BOOL'), (5, 'ENUM'), (6, 'TIMESTAMP')]),
        ),
        migrations.AlterField(
            model_name='pipelinedata',
            name='task_type',
            field=models.IntegerField(choices=[(1, 'Pruned Metrics'), (2, 'Ranked Knobs'), (3, 'Knob Data'), (4, 'Metric Data')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, verbose_name='project name'),
        ),
        migrations.AlterField(
            model_name='result',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Session', verbose_name='session name'),
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=64, verbose_name='session name'),
        ),
        migrations.AlterField(
            model_name='session',
            name='target_objective',
            field=models.CharField(choices=[('throughput_txn_per_sec', 'Throughput'), ('99th_lat_ms', '99 Percentile Latency')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='tuning_session',
            field=models.CharField(choices=[('tuning_session', 'Tuning Session'), ('no_tuning_session', 'No Tuning'), ('randomly_generate', 'Randomly Generate')], default='tuning_sesion', max_length=64),
        ),
        migrations.AlterField(
            model_name='workload',
            name='name',
            field=models.CharField(max_length=128, verbose_name='workload name'),
        ),
        migrations.AddField(
            model_name='sessionknob',
            name='knob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.KnobCatalog'),
        ),
        migrations.AddField(
            model_name='sessionknob',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Session'),
        ),
    ]
