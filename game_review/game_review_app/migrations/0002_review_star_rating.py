# Generated by Django 5.0.3 on 2024-04-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_review_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star_rating',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
