# Generated by Django 4.0.4 on 2022-05-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ziravor', '0003_xodimmodels_qabul_xodimmodels_tel_raqam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xodimmodels',
            name='tel_raqam',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
