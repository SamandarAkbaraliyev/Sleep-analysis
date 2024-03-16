# Generated by Django 4.2.7 on 2024-03-16 11:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0003_cart"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cart",
            unique_together={("user", "product")},
        ),
    ]