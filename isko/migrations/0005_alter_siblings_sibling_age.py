# Generated by Django 5.0.7 on 2024-07-13 01:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isko', '0004_alter_applicant_gwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siblings',
            name='sibling_age',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)]),
        ),
    ]
