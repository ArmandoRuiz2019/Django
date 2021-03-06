# Generated by Django 3.0.7 on 2020-06-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cursos_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentariosalumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='comentarios/foto')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['orden']},
        ),
    ]
