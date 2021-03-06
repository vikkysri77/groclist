# Generated by Django 4.0.2 on 2022-02-17 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocerieslist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='fullname',
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')], default='CH', max_length=2),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemsCount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status_options', models.CharField(choices=[('0', 'cancelled Order'), ('1', 'placed order'), ('2', 'shipped order'), ('3', 'delivered order')], max_length=1)),
                ('updatedDate', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocerieslist.client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocerieslist.item')),
            ],
        ),
    ]
