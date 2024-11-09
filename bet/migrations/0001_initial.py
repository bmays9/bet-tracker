# Generated by Django 4.2.16 on 2024-11-09 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('stake', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Win'), (-1, 'Lose')], default=0)),
                ('settled_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('punter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placed_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=16)),
                ('away_team', models.CharField(max_length=16)),
                ('prediction', models.IntegerField(choices=[(0, 'Draw'), (1, 'Home'), (2, 'Away')], default=1)),
                ('odds', models.DecimalField(decimal_places=3, max_digits=10)),
                ('match_result', models.IntegerField(choices=[(0, 'Pending'), (1, 'Win'), (-1, 'Lose')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Win'), (-1, 'Lose')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='bet.bet')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
