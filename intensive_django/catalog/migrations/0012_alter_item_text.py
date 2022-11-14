# Generated by Django 3.2.16 on 2022-11-07 16:57

import catalog.validators
from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20221107_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=markdownfield.models.MarkdownField(rendered_field='text_rendered', validators=[catalog.validators.validate_must_be_param]),
        ),
    ]