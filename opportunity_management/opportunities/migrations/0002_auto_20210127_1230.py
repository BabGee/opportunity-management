# Generated by Django 3.1.5 on 2021-01-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='ammount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
