# Generated by Django 3.1.7 on 2021-04-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210410_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='workDateTo',
            field=models.DateField(null=True),
        ),
    ]