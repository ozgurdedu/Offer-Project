# Generated by Django 4.2.5 on 2023-09-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_alter_customer_options_rfq_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]