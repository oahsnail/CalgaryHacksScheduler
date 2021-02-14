# Generated by Django 3.1.6 on 2021-02-14 00:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(unique=True)),
                ('name', models.CharField(default='Default User', max_length=30)),
                ('prefPreferedMaxConsecutiveTime', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]