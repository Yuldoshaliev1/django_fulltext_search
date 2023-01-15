# Generated by Django 4.1.5 on 2023-01-15 15:51

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('quote', models.TextField(max_length=1000)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='quote',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='apps_quote_search__607618_gin'),
        ),
    ]