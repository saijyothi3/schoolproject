# Generated by Django 3.0.5 on 2023-03-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20230301_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_performance',
            name='id',
        ),
        migrations.AlterField(
            model_name='teacher_performance',
            name='TeacherId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]