# Generated by Django 3.0.7 on 2020-11-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workexperiences', '0008_companyproject_tech_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyproject',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
