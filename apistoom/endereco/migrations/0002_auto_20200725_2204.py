# Generated by Django 3.0.8 on 2020-07-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='number',
            field=models.IntegerField(),
        ),
    ]
