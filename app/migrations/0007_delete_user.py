# Generated by Django 4.2.7 on 2023-12-09 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_user"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
    ]