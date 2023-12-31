# Generated by Django 4.1 on 2023-06-13 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Musica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("arquivo", models.FileField(upload_to="musicas/")),
                ("banda", models.CharField(max_length=200)),
                ("genero", models.CharField(max_length=100)),
                ("ano", models.IntegerField()),
            ],
        ),
    ]
