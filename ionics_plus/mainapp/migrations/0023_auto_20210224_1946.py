# Generated by Django 3.1.6 on 2021-02-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20210224_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='title',
            field=models.CharField(max_length=75),
        ),
    ]
