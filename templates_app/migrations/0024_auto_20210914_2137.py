# Generated by Django 3.2.6 on 2021-09-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_app', '0023_mailing_tag_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='notes',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_type',
            field=models.CharField(choices=[('OTH', 'Other'), ('OWN', 'Owner'), ('HELP', 'Helper'), ('DEPT', 'Department'), ('I', 'Issue'), ('ASK', 'Ask'), ('ENT', 'Entity'), ('TGT', 'Targeting'), ('CAMP', 'Camp')], default='OTH', max_length=255),
        ),
    ]