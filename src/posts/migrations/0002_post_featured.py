# Generated by Django 2.2.1 on 2019-06-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]