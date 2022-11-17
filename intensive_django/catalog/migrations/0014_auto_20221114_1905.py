# Generated by Django 3.2.16 on 2022-11-14 16:05

from django.db import migrations


def apply_text_rendered(apps, schema_editor):
    Item = apps.get_model('catalog', 'Item')
    for item in Item.objects.all():
        if not item.text_rendered:
            item.text_rendered = item.text
        item.save()


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0013_auto_20221112_2305'),
    ]

    operations = [
        migrations.RunPython(apply_text_rendered),
    ]
