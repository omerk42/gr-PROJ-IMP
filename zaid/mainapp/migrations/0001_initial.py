# Generated by Django 4.1.5 on 2023-01-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Auction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(max_length=2000)),
                (
                    "minimal_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=14),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "auctions",
            },
        ),
        migrations.CreateModel(
            name="Bid",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=14)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "bids",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.ImageField(upload_to="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "images",
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(default="default", max_length=255)),
            ],
            options={
                "db_table": "statuses",
            },
        ),
    ]
