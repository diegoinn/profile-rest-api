# Generated by Django 2.2 on 2020-10-29 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_potential_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_standard', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialSchemeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Material')),
                ('potential_type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.PotentialType')),
                ('standard_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Standard')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Unit')),
            ],
        ),
    ]
