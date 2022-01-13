# Generated by Django 4.0 on 2022-01-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('logo_number', models.IntegerField(blank=True, null=True)),
                ('logo_image', models.ImageField(upload_to='logo')),
            ],
        ),
    ]