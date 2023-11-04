# Generated by Django 3.2.8 on 2023-11-02 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20231102_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metatext',
            name='fandoms',
        ),
        migrations.CreateModel(
            name='Fandom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Nombre')),
                ('link', models.CharField(max_length=200, null=True, verbose_name='Link')),
                ('type', models.CharField(choices=[('Foro', 'Foro'), ('FanFiction', 'Fanfiction'), ('Fanart', 'Fanart'), ('Mod', 'Mod'), ('Wiki', 'Wiki'), ('Meme', 'Meme'), ('Parodia', 'Parodia')], max_length=10000)),
                ('metatext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metatext_fandoms', to='catalog.metatext')),
            ],
            options={
                'verbose_name': 'Tipo de fandom',
                'verbose_name_plural': 'Tipos de fandom',
            },
        ),
    ]
