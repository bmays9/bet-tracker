# Generated by Django 4.2.16 on 2024-11-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='match_result',
            field=models.IntegerField(choices=[(0, 'Draw'), (1, 'Home'), (2, 'Away')], default=0),
        ),
    ]
