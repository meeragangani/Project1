# Generated by Django 2.2.12 on 2020-04-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200426_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='notification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
