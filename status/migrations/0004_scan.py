# Generated by Django 4.1 on 2023-09-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_status_document_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
    ]