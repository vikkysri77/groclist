# Generated by Django 4.0.2 on 2022-02-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerieslist', '0002_remove_client_fullname_client_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]