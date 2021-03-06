# Generated by Django 3.1.6 on 2021-02-25 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_auto_20210225_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='accepted',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=75),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='file1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='file2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='file3',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='finished',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=75),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='in_progress',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=75),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='rejected',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=75),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='solving',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=75),
        ),
    ]
