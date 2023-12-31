# Generated by Django 4.2.4 on 2023-10-20 02:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_request_title', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('action', models.CharField(max_length=10)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('documents', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
    ]
