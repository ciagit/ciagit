# Generated by Django 3.1.7 on 2021-04-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='name',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
