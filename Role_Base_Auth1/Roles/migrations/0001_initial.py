# Generated by Django 2.2.7 on 2019-12-14 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='role_resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Roles.Resources')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Roles.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='role_action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Roles.Action')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Roles.Roles')),
            ],
        ),
    ]