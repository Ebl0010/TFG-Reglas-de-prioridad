# Generated by Django 2.2.dev20181219114131 on 2018-12-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nPieza', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
