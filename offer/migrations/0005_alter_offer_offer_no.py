# Generated by Django 4.2.5 on 2023-09-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_alter_offer_offer_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_no',
            field=models.CharField(max_length=25),
        ),
    ]