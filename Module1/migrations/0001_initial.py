# Generated by Django 5.0 on 2024-02-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('firstname', models.TextField(max_length=255)),
                ('lastname', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'Contactus',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'Register',
            },
        ),
    ]
