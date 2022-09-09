# Generated by Django 4.1.1 on 2022-09-09 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categoryproduct",
            name="measure_unit",
        ),
        migrations.RemoveField(
            model_name="historicalcategoryproduct",
            name="measure_unit",
        ),
        migrations.AddField(
            model_name="historicalproduct",
            name="category_product",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="products.categoryproduct",
                verbose_name="Offer indicator",
            ),
        ),
        migrations.AddField(
            model_name="historicalproduct",
            name="measure_unit",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="products.measureunit",
                verbose_name="Unit of measurement",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category_product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.categoryproduct",
                verbose_name="Offer indicator",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="measure_unit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.measureunit",
                verbose_name="Unit of measurement",
            ),
        ),
        migrations.AlterField(
            model_name="historicalofferindicator",
            name="category_product",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="products.categoryproduct",
                verbose_name="Category of product",
            ),
        ),
        migrations.AlterField(
            model_name="offerindicator",
            name="category_product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.categoryproduct",
                verbose_name="Category of product",
            ),
        ),
    ]
