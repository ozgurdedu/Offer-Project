# Generated by Django 4.2.5 on 2023-10-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0016_rename_date_rfq_request_date_rfq_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfq',
            name='rfq_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
