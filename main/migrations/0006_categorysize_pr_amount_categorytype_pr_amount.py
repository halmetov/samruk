# Generated by Django 4.0.4 on 2022-06-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_color_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorysize',
            name='pr_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='categorytype',
            name='pr_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
