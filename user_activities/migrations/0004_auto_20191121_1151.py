# Generated by Django 2.1.2 on 2019-11-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activities', '0003_auto_20181210_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
