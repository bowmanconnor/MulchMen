# Generated by Django 3.0.6 on 2020-06-07 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='key',
        ),
    ]
