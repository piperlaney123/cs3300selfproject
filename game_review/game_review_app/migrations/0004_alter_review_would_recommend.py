# Generated by Django 5.0.3 on 2024-04-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_review_app', '0003_remove_review_star_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='would_recommend',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=200),
        ),
    ]
