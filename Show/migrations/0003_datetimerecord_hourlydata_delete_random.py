# Generated by Django 4.2.9 on 2024-01-25 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0002_random_update_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateTimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HourlyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_1_data', models.FloatField(blank=True, null=True)),
                ('hour_2_data', models.FloatField(blank=True, null=True)),
                ('hour_3_data', models.FloatField(blank=True, null=True)),
                ('hour_4_data', models.FloatField(blank=True, null=True)),
                ('hour_5_data', models.FloatField(blank=True, null=True)),
                ('hour_6_data', models.FloatField(blank=True, null=True)),
                ('hour_7_data', models.FloatField(blank=True, null=True)),
                ('hour_8_data', models.FloatField(blank=True, null=True)),
                ('hour_9_data', models.FloatField(blank=True, null=True)),
                ('hour_10_data', models.FloatField(blank=True, null=True)),
                ('hour_11_data', models.FloatField(blank=True, null=True)),
                ('hour_12_data', models.FloatField(blank=True, null=True)),
                ('hour_13_data', models.FloatField(blank=True, null=True)),
                ('hour_14_data', models.FloatField(blank=True, null=True)),
                ('hour_15_data', models.FloatField(blank=True, null=True)),
                ('hour_16_data', models.FloatField(blank=True, null=True)),
                ('hour_17_data', models.FloatField(blank=True, null=True)),
                ('hour_18_data', models.FloatField(blank=True, null=True)),
                ('hour_19_data', models.FloatField(blank=True, null=True)),
                ('hour_20_data', models.FloatField(blank=True, null=True)),
                ('hour_21_data', models.FloatField(blank=True, null=True)),
                ('hour_22_data', models.FloatField(blank=True, null=True)),
                ('hour_23_data', models.FloatField(blank=True, null=True)),
                ('hour_24_data', models.FloatField(blank=True, null=True)),
                ('datetime_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Show.datetimerecord')),
            ],
        ),
        migrations.DeleteModel(
            name='Random',
        ),
    ]