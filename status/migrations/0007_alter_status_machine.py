# Generated by Django 4.1 on 2023-10-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0006_remove_scan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='status.machine'),
        ),
    ]
