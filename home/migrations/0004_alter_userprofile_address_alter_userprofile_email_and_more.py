# Generated by Django 4.2.4 on 2023-09-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_userprofile_address_alter_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='address', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='username@gmail.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='job_profile',
            field=models.CharField(default='Job profile', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='username', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='url1',
            field=models.URLField(default='url', max_length=50),
        ),
    ]
