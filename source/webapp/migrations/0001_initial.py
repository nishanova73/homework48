# Generated by Django 4.0.1 on 2022-01-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('detailed_description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='detailed_description')),
                ('category', models.CharField(choices=[('other', 'other'), ('fruits', 'fruits'), ('milk', 'milk'), ('chocolate', 'chocolate'), ('coffee', 'coffee')], default='other', max_length=15)),
                ('remainder', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name': 'good',
                'verbose_name_plural': 'goods',
                'db_table': 'Goods',
            },
        ),
    ]