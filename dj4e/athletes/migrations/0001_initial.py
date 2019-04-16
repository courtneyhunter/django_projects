# Generated by Django 2.1.7 on 2019-03-01 02:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Sport must be greater than 1 character')])),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a sport (e.g. Dodge)', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Sport must be greater than 1 character')])),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Sport'),
        ),
    ]
