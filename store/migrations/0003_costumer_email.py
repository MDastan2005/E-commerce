# Generated by Django 4.1.7 on 2023-02-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
