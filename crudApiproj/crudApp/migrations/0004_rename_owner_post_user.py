# Generated by Django 4.2.4 on 2023-08-06 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_remove_userprofile_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='user',
        ),
    ]
