# Generated by Django 4.1.5 on 2023-01-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='avatar', verbose_name='photo de profile'),
        ),
    ]
