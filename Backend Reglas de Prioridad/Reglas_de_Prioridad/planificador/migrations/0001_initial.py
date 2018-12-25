# Generated by Django 2.1.4 on 2018-12-11 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True
    atomic = False
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('nFase', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('nMaquina', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('nPieza', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Maquinas_Ejecutadas',
            fields=[
                ('maquinaNecesaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='planificador.Maquina')),
            ],
        ),
        migrations.AddField(
            model_name='fase',
            name='maquinaNecesaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificador.Maquina'),
        ),
        migrations.AddField(
            model_name='fase',
            name='nPieza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificador.Pieza'),
        ),
        migrations.AddField(
            model_name='maquinas_ejecutadas',
            name='nFase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificador.Fase'),
        ),
        migrations.AddField(
            model_name='maquinas_ejecutadas',
            name='nPieza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificador.Pieza'),
        ),
    ]
