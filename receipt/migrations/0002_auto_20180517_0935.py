# Generated by Django 2.0.5 on 2018-05-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
