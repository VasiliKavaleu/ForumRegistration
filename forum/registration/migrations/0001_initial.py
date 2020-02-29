# Generated by Django 3.0.3 on 2020-02-29 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=238)),
                ('theme_extended', models.CharField(blank=True, max_length=238)),
                ('detail_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('tel', models.IntegerField(max_length=30)),
                ('address', models.EmailField(max_length=254)),
            ],
        ),
    ]