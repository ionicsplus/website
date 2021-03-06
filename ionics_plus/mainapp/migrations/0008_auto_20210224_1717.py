# Generated by Django 3.1.6 on 2021-02-24 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0007_auto_20210224_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='country',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='email',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='services',
            field=models.CharField(choices=[('Home Work', 'Home Work'), ('Project', 'Project'), ('Course', 'Course')], max_length=75),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='solving',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='subject',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='title',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='whatsapp_number',
            field=models.IntegerField(null=True),
        ),
    ]
