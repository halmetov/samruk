# Generated by Django 4.0.4 on 2022-06-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_color_col_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
