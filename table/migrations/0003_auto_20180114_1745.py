# Generated by Django 2.0.1 on 2018-01-14 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20180114_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationstatus',
            old_name='floor',
            new_name='floor_table_no',
        ),
        migrations.RemoveField(
            model_name='reservationstatus',
            name='table_no',
        ),
    ]
