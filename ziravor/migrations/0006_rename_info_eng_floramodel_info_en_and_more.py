# Generated by Django 4.0.4 on 2022-05-30 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ziravor', '0005_rename_qabul_xodimmodels_fullname_eng_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floramodel',
            old_name='info_eng',
            new_name='info_en',
        ),
        migrations.RenameField(
            model_name='floramodel',
            old_name='name_eng',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='floramodel',
            old_name='subtitle_eng',
            new_name='subtitle_en',
        ),
        migrations.RenameField(
            model_name='floramodel',
            old_name='title_eng',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='floratypemodel',
            old_name='type_eng',
            new_name='type_en',
        ),
        migrations.RenameField(
            model_name='xodimmodels',
            old_name='fullname_eng',
            new_name='fullname_en',
        ),
        migrations.RenameField(
            model_name='xodimmodels',
            old_name='lavozim_eng',
            new_name='lavozim_en',
        ),
        migrations.RenameField(
            model_name='xodimmodels',
            old_name='qabul_eng',
            new_name='qabul_en',
        ),
        migrations.RenameField(
            model_name='yangiliklarmodel',
            old_name='sub_title_eng',
            new_name='sub_title_en',
        ),
        migrations.RenameField(
            model_name='yangiliklarmodel',
            old_name='text_eng',
            new_name='text_en',
        ),
        migrations.RenameField(
            model_name='yangiliklarmodel',
            old_name='title_eng',
            new_name='title_en',
        ),
    ]