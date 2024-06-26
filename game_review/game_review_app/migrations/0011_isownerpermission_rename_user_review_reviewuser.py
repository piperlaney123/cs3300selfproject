# Generated by Django 5.0.3 on 2024-04-18 00:52

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('game_review_app', '0010_rename_user_reviewuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsOwnerPermission',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='reviewuser',
        ),
    ]
