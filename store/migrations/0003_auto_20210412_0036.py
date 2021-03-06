# Generated by Django 3.1.7 on 2021-04-11 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rem_quant',
            field=models.PositiveIntegerField(default=0, verbose_name='quantity remaining'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='unitprice',
            field=models.PositiveIntegerField(default=0, verbose_name='Price'),
            preserve_default=False,
        ),
    ]
