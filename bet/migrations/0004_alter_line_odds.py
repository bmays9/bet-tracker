# Generated by Django 4.2.16 on 2024-11-22 19:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_alter_line_match_result_alter_line_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='odds',
            field=models.DecimalField(decimal_places=3, max_digits=10, validators=[django.core.validators.MinValueValidator(1.01)]),
        ),
    ]