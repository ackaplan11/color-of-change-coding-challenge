# Generated by Django 3.2 on 2021-06-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_app', '0019_merge_20210521_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='ak_wrapper_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
