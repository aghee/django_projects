# Generated by Django 5.0.5 on 2024-05-08 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_product_product_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default=3, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='alternative_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.producttype'),
        ),
        migrations.AlterField(
            model_name='seasonalevents',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
