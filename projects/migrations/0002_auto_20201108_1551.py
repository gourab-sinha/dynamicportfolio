# Generated by Django 3.0.7 on 2020-11-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]