# Generated by Django 4.2 on 2023-08-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_active',
            field=models.BooleanField(default=False, verbose_name='邮箱激活状态'),
        ),
    ]
