# Generated by Django 2.2.3 on 2019-07-02 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareimg', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageShare',
            new_name='SharedImage',
        ),
    ]
