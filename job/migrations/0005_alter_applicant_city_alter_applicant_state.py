# Generated by Django 4.2.8 on 2023-12-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_applicant_city_applicant_state_applicant_zip_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
