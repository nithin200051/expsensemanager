# Generated by Django 4.1.1 on 2023-02-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_profile_delete_persons'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=False),
        ),
    ]
