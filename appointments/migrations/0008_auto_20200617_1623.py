# Generated by Django 3.0.7 on 2020-06-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_auto_20200611_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]