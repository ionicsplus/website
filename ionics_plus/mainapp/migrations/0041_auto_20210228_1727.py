# Generated by Django 3.1.6 on 2021-02-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_user_service_solution_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='solution_file',
            field=models.FileField(upload_to=''),
        ),
    ]
