# Generated by Django 3.2 on 2021-04-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing_choice', models.CharField(choices=[('shoes', 'SHOES'), ('shirt', 'SHIRT'), ('jeans', 'JEANS'), ('polo', 'POLO')], max_length=8)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('model_clothing', models.CharField(max_length=12, verbose_name='Name model')),
                ('price', models.IntegerField(default=10, verbose_name='Price')),
                ('color', models.CharField(blank=True, max_length=20, verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name Fabric')),
                ('about_us', models.TextField(verbose_name='About as')),
            ],
        ),
    ]
