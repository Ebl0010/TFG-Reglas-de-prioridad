# Generated by Django 2.1.4 on 2019-01-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0013_resultadogeneral_ejecucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadogeneral',
            name='ejecucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pieza.Ejecucion'),
        ),
        migrations.AlterField(
            model_name='resultadogeneral',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
