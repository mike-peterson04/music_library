# Generated by Django 3.1.8 on 2021-05-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(),
        ),
    ]