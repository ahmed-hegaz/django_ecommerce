# Generated by Django 3.1.4 on 2020-12-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20201227_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDslug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
