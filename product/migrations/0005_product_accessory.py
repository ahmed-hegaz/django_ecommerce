# Generated by Django 3.1.4 on 2020-12-26 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201226_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternative', models.ManyToManyField(related_name='accessories_product', to='product.Product', verbose_name='accessory product')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_Product', to='product.product')),
            ],
            options={
                'verbose_name': 'Product Accessory',
                'verbose_name_plural': 'Product Accessories',
            },
        ),
    ]
