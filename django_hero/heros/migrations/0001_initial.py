# Generated by Django 3.1.2 on 2020-10-26 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField(blank=True)),
                ('created_datetime', models.DateTimeField()),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
