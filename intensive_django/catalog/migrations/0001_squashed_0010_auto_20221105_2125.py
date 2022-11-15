# Generated by Django 3.2.16 on 2022-11-13 12:27

import re

import django.core.validators
import django.db.models.deletion
import markdownfield.models
from django.db import migrations, models

import catalog.validators


class Migration(migrations.Migration):

    replaces = [('catalog', '0001_initial'), ('catalog', '0002_auto_20221031_1654'), ('catalog', '0003_alter_item_text'), ('catalog', '0004_alter_item_text'), ('catalog', '0005_alter_item_text'), ('catalog', '0006_alter_item_text'), ('catalog', '0007_alter_item_text'), ('catalog', '0008_auto_20221105_2039'), ('catalog', '0009_auto_20221105_2121'), ('catalog', '0010_auto_20221105_2125')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('weight', models.SmallIntegerField(default=100)),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('text', markdownfield.models.MarkdownField(rendered_field='text_rendered', validators=[catalog.validators.validate_must_be_param])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category')),
                ('tags', models.ManyToManyField(related_name='items', to='catalog.Tag')),
                ('text_rendered', markdownfield.models.RenderedMarkdownField(default='')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
            ],
            options={
                'verbose_name': 'Главное изображение',
                'verbose_name_plural': 'Главные изображения',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.item')),
            ],
            options={
                'verbose_name': 'Главное изображение',
                'verbose_name_plural': 'Главные изображения',
            },
        ),
    ]
