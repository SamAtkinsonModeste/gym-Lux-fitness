# Generated by Django 4.2.19 on 2025-02-10 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclasses', '0002_alter_gymclasses_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gymclasses',
            old_name='description',
            new_name='content',
        ),
    ]
