# Generated by Django 4.0.5 on 2022-06-22 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='building.apartment')),
            ],
            options={
                'verbose_name': 'Owner',
                'verbose_name_plural': 'Owners',
                'ordering': ('-created',),
            },
        ),
    ]
