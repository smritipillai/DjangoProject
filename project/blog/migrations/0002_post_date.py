# Generated by Django 2.2.1 on 2019-05-28 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
