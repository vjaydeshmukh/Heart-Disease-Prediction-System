# Generated by Django 2.2.1 on 2019-08-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0004_auto_20190812_1913'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.AlterField(
            model_name='heart',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='heart',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='heart',
            name='sex',
            field=models.IntegerField(default=0),
        ),
    ]
