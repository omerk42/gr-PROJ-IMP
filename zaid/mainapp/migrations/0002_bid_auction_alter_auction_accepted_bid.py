# Generated by Django 4.1.5 on 2023-01-10 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="auction",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="auction",
                to="mainapp.auction",
            ),
        ),
        migrations.AlterField(
            model_name="auction",
            name="accepted_bid",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accepted_bid",
                to="mainapp.bid",
            ),
        ),
    ]