# Generated by Django 4.0 on 2021-12-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_customers',
            },
        ),
    ]
