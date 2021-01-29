# Generated by Django 3.1.5 on 2021-01-27 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ammount', models.IntegerField()),
                ('stage', models.CharField(choices=[('D', 'Discovery'), ('P', 'Proposal shared'), ('N', 'Negotiations')], default='D', max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunities.account')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]