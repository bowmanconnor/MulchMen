# Generated by Django 3.0.6 on 2020-06-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_appointment_bed_cleaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, default='example@example.com', max_length=254),
        ),
    ]