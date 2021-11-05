# Generated by Django 3.1.7 on 2021-03-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_app', '0007_tag_tag_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='source_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_type',
            field=models.CharField(choices=[('OTH', 'Other'), ('OWN', 'Owner'), ('DEPT', 'Department'), ('I', 'Issue'), ('ASK', 'Ask'), ('ENT', 'Entity'), ('TGT', 'Targeting'), ('CAMP', 'Camp')], default='OTH', max_length=255),
        ),
    ]
