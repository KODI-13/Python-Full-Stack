# Generated by Django 4.2.5 on 2023-09-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
