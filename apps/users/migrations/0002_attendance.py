# Generated by Django 5.1.5 on 2025-02-19 03:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('work_time', models.TimeField()),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('late_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Davomat',
                'verbose_name_plural': 'Davomatlar',
                'unique_together': {('user', 'date')},
            },
        ),
    ]
