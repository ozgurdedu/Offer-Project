# Generated by Django 4.2.5 on 2023-10-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_customer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfq',
            name='srv_rfq_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
