# Generated by Django 2.2.12 on 2020-04-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='uploadfile',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
