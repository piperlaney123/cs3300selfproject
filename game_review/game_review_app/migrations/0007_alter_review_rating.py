# Generated by Django 5.0.3 on 2024-04-04 00:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_review_app', '0006_review_rating_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]