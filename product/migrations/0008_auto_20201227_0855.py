# Generated by Django 3.1.4 on 2020-12-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20201227_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='PRDimage',
            new_name='PRDIimage',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='PRDproduct',
            new_name='PRDIproduct',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDimage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='product image'),
        ),
    ]