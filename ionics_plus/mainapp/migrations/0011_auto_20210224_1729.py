# Generated by Django 3.1.6 on 2021-02-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210224_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='title',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
