# Generated by Django 5.0.4 on 2024-04-14 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FutureRequest',
            new_name='FeatureRequest',
        ),
    ]