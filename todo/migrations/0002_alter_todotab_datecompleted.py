# Generated by Django 3.2.6 on 2021-08-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotab',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]