# Generated by Django 2.1.7 on 2019-03-20 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1000)),
                ('justification', models.CharField(max_length=1000)),
                ('year', models.IntegerField(null=True)),
                ('longtitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('area', models.FloatField(null=True)),
                ('category', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Category')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
            ],
        ),
    ]
