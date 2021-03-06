# Generated by Django 3.0.7 on 2020-11-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workexperiences', '0010_auto_20201109_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='projects',
            field=models.ManyToManyField(blank=True, to='workexperiences.CompanyProject'),
        ),
        migrations.AlterField(
            model_name='company',
            name='techs',
            field=models.ManyToManyField(blank=True, to='workexperiences.Technology'),
        ),
    ]
