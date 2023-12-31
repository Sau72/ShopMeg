# Generated by Django 4.2 on 2023-05-23 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basket",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="app_order.order",
                verbose_name="Заказ",
            ),
        ),
    ]
