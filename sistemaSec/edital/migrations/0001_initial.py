# Generated by Django 3.2.11 on 2022-06-13 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id_edital', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade_vagas_edital', models.IntegerField()),
                ('id_programa_edital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='editais', to='programa.programa')),
            ],
        ),
    ]
