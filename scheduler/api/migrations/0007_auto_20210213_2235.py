# Generated by Django 3.1.6 on 2021-02-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210213_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedtask',
            name='taskName',
            field=models.CharField(default='fixedtask', max_length=30),
        ),
    ]
