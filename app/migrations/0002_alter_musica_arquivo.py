# Generated by Django 4.1 on 2023-06-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="musica",
            name="arquivo",
            field=models.FileField(upload_to="media/"),
        ),
    ]
