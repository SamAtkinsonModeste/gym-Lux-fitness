# Generated by Django 4.2.19 on 2025-02-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymclasses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymclasses',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
