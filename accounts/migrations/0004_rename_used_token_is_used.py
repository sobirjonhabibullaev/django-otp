# Generated by Django 4.0.4 on 2022-05-28 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='used',
            new_name='is_used',
        ),
    ]
