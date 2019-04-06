# Generated by Django 2.1.7 on 2019-03-01 15:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a house (e.g. Dodge)', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'House must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'House must be greater than 1 character')])),
                ('power', models.PositiveIntegerField()),
                ('spell', models.CharField(max_length=300)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizards.House')),
            ],
        ),
    ]
