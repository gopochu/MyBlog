# Generated by Django 4.1.5 on 2023-01-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='vadich',
            field=models.CharField(max_length=255, null=True, verbose_name='просто вадич'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
