# Generated by Django 4.0.10 on 2023-10-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('accounting_period', models.CharField(max_length=255)),
                ('scope_1', models.IntegerField(blank=True, null=True)),
                ('scope_2', models.IntegerField(blank=True, null=True)),
                ('scope_3', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
