# Generated by Django 4.2.6 on 2023-10-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('cat_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cat_percentile', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
