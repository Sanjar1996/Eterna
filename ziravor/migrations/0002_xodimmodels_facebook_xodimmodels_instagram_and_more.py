# Generated by Django 4.0.4 on 2022-05-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ziravor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xodimmodels',
            name='facebook',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='xodimmodels',
            name='instagram',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='xodimmodels',
            name='telegram',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]