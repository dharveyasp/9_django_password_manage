# Generated by Django 4.1.7 on 2023-03-30 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0004_rename_storedpasswords_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='password',
            name='pass_word',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='password',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='password',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]