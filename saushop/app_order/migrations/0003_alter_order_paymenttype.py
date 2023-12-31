# Generated by Django 4.2 on 2023-05-23 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_order", "0002_alter_basket_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="paymentType",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="paymentType",
                to="app_order.payment",
                verbose_name="Способ оплаты",
            ),
        ),
    ]
