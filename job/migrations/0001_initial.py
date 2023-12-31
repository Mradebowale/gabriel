# Generated by Django 4.2.8 on 2023-12-09 14:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_name', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=100)),
                ('Home_address', models.CharField(max_length=300)),
                ('Phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('Job_aspired', models.CharField(choices=[('PA', 'Personal assistant'), ('DA', 'Data Entry'), ('MS', 'Mystery Shopper'), ('VA', 'Virtual Assistant')], max_length=100)),
                ('Id_document', models.CharField(choices=[('DL', "Driver's License"), ('PP', 'Passport'), ('SID', 'State ID')], max_length=100)),
                ('Id_image', models.ImageField(blank=True, null=True, upload_to='Documents')),
                ('Former_workplace', models.CharField(blank=True, max_length=200, null=True)),
                ('Workplace_address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('salary', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Remote', 'Remote'), ('On site', 'On site')], max_length=200)),
            ],
        ),
    ]
