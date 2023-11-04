# Generated by Django 3.2.8 on 2023-11-02 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_hipotext_innecesary_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentarysource',
            options={'verbose_name': 'Fuente documental', 'verbose_name_plural': 'Fuentes documentales'},
        ),
        migrations.RemoveField(
            model_name='metatext',
            name='blogs',
        ),
        migrations.RemoveField(
            model_name='metatext',
            name='criticism',
        ),
        migrations.RemoveField(
            model_name='metatext',
            name='declarations',
        ),
        migrations.RemoveField(
            model_name='metatext',
            name='press_articles',
        ),
        migrations.RemoveField(
            model_name='metatext',
            name='social_networks',
        ),
        migrations.AddField(
            model_name='metatext',
            name='innecesary_field',
            field=models.IntegerField(choices=[(1, 1)], default=1, verbose_name='Campo innecesario solo para funcionamiento'),
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000, verbose_name='Descripción')),
                ('link', models.CharField(max_length=10000, verbose_name='Link')),
                ('metatext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metatext_social_networks', to='catalog.metatext')),
            ],
            options={
                'verbose_name': 'Social Network',
                'verbose_name_plural': 'Social Networks',
            },
        ),
        migrations.CreateModel(
            name='PressArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000, verbose_name='Descripción')),
                ('link', models.CharField(max_length=10000, verbose_name='Link')),
                ('metatext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metatext_press_article', to='catalog.metatext')),
            ],
            options={
                'verbose_name': 'Artículo de prensa',
                'verbose_name_plural': 'Artículos de prensa',
            },
        ),
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000, verbose_name='Descripción')),
                ('link', models.CharField(max_length=10000, verbose_name='Link')),
                ('metatext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metatext_declarations', to='catalog.metatext')),
            ],
            options={
                'verbose_name': 'Declaración autorizada',
                'verbose_name_plural': 'Declaraciones autorizadas',
            },
        ),
        migrations.CreateModel(
            name='Criticism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000, verbose_name='Descripción')),
                ('link', models.CharField(max_length=10000, verbose_name='Link')),
                ('metatext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metatext_criticism', to='catalog.metatext')),
            ],
            options={
                'verbose_name': 'Crítica',
                'verbose_name_plural': 'Críticas',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000, verbose_name='Descripción')),
                ('link', models.CharField(max_length=10000, verbose_name='Link')),
                ('metatext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metatext_blogs', to='catalog.metatext')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]