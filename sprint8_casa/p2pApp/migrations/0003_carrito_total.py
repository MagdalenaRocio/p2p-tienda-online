# Generated by Django 2.2.10 on 2020-03-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2pApp', '0002_carrito_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]