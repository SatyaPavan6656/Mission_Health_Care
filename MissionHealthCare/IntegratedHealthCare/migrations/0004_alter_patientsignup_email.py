# Generated by Django 5.0.6 on 2024-07-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IntegratedHealthCare', '0003_patientsignup_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsignup',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
