# Generated by Django 3.2.11 on 2022-06-13 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programa', '0001_initial'),
        ('edital', '0001_initial'),
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estagio',
            fields=[
                ('id_estagio', models.AutoField(primary_key=True, serialize=False)),
                ('carga_horaria_estagio', models.IntegerField()),
                ('area_estagio', models.CharField(max_length=200)),
                ('id_cursos_estagio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estagios', to='curso.curso')),
                ('id_edital_estagio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estagios', to='edital.edital')),
                ('id_programa_estagio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estagios', to='programa.programa')),
            ],
        ),
    ]