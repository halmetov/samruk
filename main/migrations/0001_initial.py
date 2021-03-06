# Generated by Django 4.0.4 on 2022-06-10 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('is_main', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('is_main', models.BooleanField()),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catalog')),
            ],
        ),
        migrations.CreateModel(
            name='CategorySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('is_main', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('is_main', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('is_main', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('rating', models.FloatField(default=0.0)),
                ('views', models.IntegerField(default=0)),
                ('short_description', models.TextField()),
                ('old_price', models.IntegerField(default=0)),
                ('new_price', models.IntegerField(default=0)),
                ('weight', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('details', models.TextField()),
                ('logo', models.ImageField(upload_to='upload')),
                ('discount', models.IntegerField(default=0)),
                ('is_new', models.BooleanField()),
                ('is_best_seller', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorysize')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('is_main', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.AddField(
            model_name='categorysize',
            name='categorytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorytype'),
        ),
    ]
