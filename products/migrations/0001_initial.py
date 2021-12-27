# Generated by Django 4.0 on 2021-12-26 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField(default=1)),
                ('unit', models.CharField(choices=[('', 'Choose Product Unit'), ('l', 'litre'), ('pcs', 'pcs'), ('gm', 'gm'), ('ml', 'ml')], default='', max_length=50)),
                ('category', models.CharField(choices=[('indoor service', 'indoor service'), ('outdoor service', 'outdoor service')], max_length=200, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'tbl_products',
            },
        ),
        migrations.CreateModel(
            name='HistConf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual', models.PositiveSmallIntegerField()),
                ('transition', models.IntegerField()),
                ('total', models.PositiveSmallIntegerField()),
                ('user', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]