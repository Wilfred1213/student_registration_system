# Generated by Django 4.2.9 on 2024-06-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0011_alter_estudiante_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='estudiantes_en_la_misma_casa',
            field=models.ManyToManyField(blank=True, help_text='Ingrese estudiantes que viven en la misma casa.', to='personas.estudiante'),
        ),
    ]
