# Generated by Django 4.1.3 on 2022-12-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='Descripcion_del_Proyecto',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='Tags',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='Titulo_del_Proyecto',
        ),
        migrations.AddField(
            model_name='formulario',
            name='Foto',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='formulario',
            name='Titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='formulario',
            name='descripcion',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='formulario',
            name='tags',
            field=models.CharField(default='', max_length=100),
        ),
    ]