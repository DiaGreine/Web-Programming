# Generated by Django 3.0 on 2019-12-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('categories', models.CharField(max_length=10)),
                ('rating', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
