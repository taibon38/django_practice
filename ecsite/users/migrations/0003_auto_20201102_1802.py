# Generated by Django 3.1.2 on 2020-11-02 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_fav_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='poit',
            new_name='point',
        ),
    ]