# Generated by Django 3.1.6 on 2021-02-14 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210213_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedtask',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
