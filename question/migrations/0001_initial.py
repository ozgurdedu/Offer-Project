# Generated by Django 4.2.5 on 2023-09-28 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0008_customer_logo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=255)),
                ('answer_1', models.TextField(blank=True, max_length=255, null=True)),
                ('answer_2', models.TextField(blank=True, max_length=255, null=True)),
                ('answer_3', models.TextField(blank=True, max_length=255, null=True)),
                ('answer_4', models.TextField(blank=True, max_length=255, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('question_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_creator', to=settings.AUTH_USER_MODEL)),
                ('related_person', models.ManyToManyField(related_name='related_questions', to=settings.AUTH_USER_MODEL)),
                ('rfq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.rfq')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=255, null=True)),
                ('comment_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_answer_creator', to='question.answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.comment'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question'),
        ),
    ]
