# Generated by Django 4.0 on 2022-02-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Username',
            field=models.CharField(max_length=100, primary_key=b'I01\n', serialize=False),
        ),
    ]