# Generated by Django 5.0.6 on 2024-07-10 05:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkyColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='skys/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('BL', 'BLUE'), ('YE', 'YELLOW'), ('RE', 'RED'), ('OR', 'ORANGE'), ('PI', 'PINK')], max_length=2)),
            ],
        ),
    ]
