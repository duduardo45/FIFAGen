# Generated by Django 3.2.13 on 2023-12-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIFAGen', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='players',
            field=models.ManyToManyField(to='FIFAGen.PlayerInBase'),
        ),
    ]
