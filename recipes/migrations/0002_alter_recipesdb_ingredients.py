# Generated by Django 4.2.21 on 2025-05-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesdb',
            name='ingredients',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
