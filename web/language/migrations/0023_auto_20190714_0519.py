# Generated by Django 2.2.3 on 2019-07-14 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0022_auto_20190714_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='language',
            new_name='languages',
        ),
    ]
