# Generated by Django 4.0.6 on 2022-07-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
