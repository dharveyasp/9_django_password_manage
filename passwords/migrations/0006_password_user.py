# Generated by Django 4.1.7 on 2023-03-30 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passwords', '0005_alter_password_description_alter_password_pass_word_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to=settings.AUTH_USER_MODEL),
        ),
    ]
