# Generated by Django 2.1.7 on 2019-03-01 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_auto_20190301_0315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='weight',
            new_name='age',
        ),
    ]