# Generated by Django 5.0.3 on 2024-04-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_review_app', '0004_alter_review_would_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='would_recommend',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200),
        ),
    ]
