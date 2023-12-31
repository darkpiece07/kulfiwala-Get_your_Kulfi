# Generated by Django 4.2.4 on 2023-09-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userprofile_address_alter_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='static/avatar.png', height_field=200, upload_to='profile_pics/', width_field=200),
        ),
    ]
