# Generated by Django 2.2.12 on 2020-05-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_feedback_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
