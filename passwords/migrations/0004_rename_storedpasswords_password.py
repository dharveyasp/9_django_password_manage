# Generated by Django 4.1.7 on 2023-03-30 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0003_alter_storedpasswords_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StoredPasswords',
            new_name='Password',
        ),
    ]
