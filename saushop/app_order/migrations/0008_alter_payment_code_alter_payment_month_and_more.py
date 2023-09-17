# Generated by Django 4.2 on 2023-05-24 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app_profile", "0001_initial"),
        ("app_order", "0007_alter_payment_options_payment_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="code",
            field=models.CharField(
                default=None, max_length=20, null=True, verbose_name="Код"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="month",
            field=models.CharField(
                default=None, max_length=20, null=True, verbose_name="Месяц"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="name",
            field=models.CharField(
                default=None, max_length=20, null=True, verbose_name="Имя владельца"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="number",
            field=models.CharField(
                default=None, max_length=20, null=True, verbose_name="Оплата"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="app_profile.profile",
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="year",
            field=models.CharField(
                default=None, max_length=20, null=True, verbose_name="Год"
            ),
        ),
    ]
