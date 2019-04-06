# Generated by Django 2.1.7 on 2019-03-20 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='states',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='iso',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='region',
            name='region',
        ),
        migrations.RemoveField(
            model_name='site',
            name='area',
        ),
        migrations.RemoveField(
            model_name='site',
            name='longtitude',
        ),
        migrations.AddField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='iso',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.category'),
        ),
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='site',
            name='iso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.iso'),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.region'),
        ),
        migrations.AlterField(
            model_name='site',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.states'),
        ),
    ]