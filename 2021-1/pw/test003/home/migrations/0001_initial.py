# Generated by Django 3.1.7 on 2021-03-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('ID', models.IntegerField()),
            ],
        ),
    ]
