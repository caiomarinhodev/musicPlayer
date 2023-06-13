# Generated by Django 4.1 on 2023-06-13 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_musica_arquivo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="musica",
            name="ano",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="musica",
            name="banda",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="musica",
            name="genero",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]