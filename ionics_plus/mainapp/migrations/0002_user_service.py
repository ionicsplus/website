# Generated by Django 3.1.6 on 2021-02-22 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('services', models.CharField(choices=[('Home Work', 'Home Work'), ('Project', 'Project'), ('Course', 'Course')], max_length=75)),
                ('subject', models.TextField()),
                ('email', models.CharField(max_length=75, null=True)),
                ('whatsapp_number', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=75, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('solving', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('in_progress', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
