# Generated by Django 5.1.5 on 2025-02-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('come', 'Kelgan'), ('absent', 'Kelmagan'), ('late', 'Kech kelgan')], default='absent', max_length=20),
        ),
    ]
