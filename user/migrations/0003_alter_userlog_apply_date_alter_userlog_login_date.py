# Generated by Django 4.0.5 on 2022-06-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='apply_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='login_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]