# Generated by Django 3.2.10 on 2022-07-17 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0005_alter_niveleducativo_options'),
        ('disciplina', '0002_alter_faltadisciplinariaestudiantil_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='faltadisciplinariaestudiantil',
            name='periodo_escolar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='escuela.periodoescolar'),
            preserve_default=False,
        ),
    ]
