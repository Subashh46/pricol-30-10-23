# Generated by Django 4.1 on 2023-06-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
