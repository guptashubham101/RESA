# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractedRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('recipe_template', models.TextField()),
                ('recipe_url', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modification_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=50)),
                ('recipe_title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'extracted_recipe',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ingredient_name', models.CharField(max_length=50)),
                ('recipeId', models.ForeignKey(to='app.ExtractedRecipe')),
            ],
            options={
                'db_table': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modification_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='extractedrecipe',
            name='userId',
            field=models.ForeignKey(to='app.User'),
        ),
    ]
