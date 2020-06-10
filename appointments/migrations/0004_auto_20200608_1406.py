# Generated by Django 3.0.6 on 2020-06-08 18:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_remove_appointment_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='additional_comments',
            field=models.CharField(blank=True, help_text='Type of mulch, delivery instructions, quantity of mulch confusion, special requests, etc', max_length=2000),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Not required. +1 before phone number', max_length=128, region='US'),
        ),
    ]