# Generated by Django 3.2.13 on 2023-11-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInBase',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('playerKeys', models.JSONField()),
            ],
        ),
    ]
