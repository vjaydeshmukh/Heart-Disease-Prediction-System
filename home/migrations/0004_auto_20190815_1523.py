# Generated by Django 2.2.1 on 2019-08-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190815_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
