# Generated by Django 2.1.4 on 2019-01-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0012_piezaresultado_algoritmo'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadogeneral',
            name='ejecucion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
