# Generated by Django 4.2.2 on 2023-06-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='model',
            options={'verbose_name': 'Model', 'verbose_name_plural': 'Models'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='model',
            name='body_style',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'HatchBack'), ('liftback', 'Liftback'), ('coupe', 'Coupe'), ('crossover', 'Crossover'), ('truck', 'Truck'), ('wagon', 'Wagon')], max_length=100),
        ),
        migrations.AlterField(
            model_name='model',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]