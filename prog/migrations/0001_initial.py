# Generated by Django 4.0 on 2022-03-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('orderid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('totalprice', models.CharField(max_length=10)),
            ],
        ),
    ]
