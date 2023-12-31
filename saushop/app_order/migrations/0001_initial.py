# Generated by Django 4.2 on 2023-05-23 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_profile", "0001_initial"),
        ("app_shop", "0003_delete_basket"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=20, verbose_name="Оплата")),
                ("month", models.CharField(max_length=20, verbose_name="Месяц")),
                ("year", models.CharField(max_length=20, verbose_name="Год")),
                ("code", models.CharField(max_length=20, verbose_name="Код")),
                (
                    "name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="app_profile.profile",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "способ оплаты",
                "verbose_name_plural": "способы оплаты",
                "db_table": "payments",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "createdAt",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "deliveryType",
                    models.CharField(
                        default="ordinary", max_length=120, verbose_name="Доставка"
                    ),
                ),
                (
                    "totalCost",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=12,
                        verbose_name="Общая стоимость",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default=False, max_length=20, verbose_name="Статус"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default=None, max_length=100, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        default=None, max_length=120, null=True, verbose_name="Адрес"
                    ),
                ),
                (
                    "paymentType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paymentType",
                        to="app_order.payment",
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_order",
                        to="app_profile.profile",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "заказ",
                "verbose_name_plural": "заказы",
                "db_table": "orders",
                "ordering": ["-createdAt", "-status"],
            },
        ),
        migrations.CreateModel(
            name="Basket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=1000000,
                        verbose_name="цена",
                    ),
                ),
                (
                    "count",
                    models.PositiveIntegerField(default=0, verbose_name="количество"),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="app_order.order",
                        verbose_name="Заказ",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product",
                        to="app_shop.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "корзина",
                "verbose_name_plural": "корзины",
                "ordering": ["-product"],
            },
        ),
    ]
