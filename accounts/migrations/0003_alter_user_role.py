# Generated by Django 4.2 on 2023-04-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Customer'), (1, 'Restaurant')], null=True),
        ),
    ]
