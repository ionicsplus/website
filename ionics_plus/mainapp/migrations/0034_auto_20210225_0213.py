# Generated by Django 3.1.6 on 2021-02-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_auto_20210225_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='file1',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='file2',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='file3',
            field=models.FileField(upload_to=''),
        ),
    ]
