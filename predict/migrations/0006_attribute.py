# Generated by Django 2.2.1 on 2019-08-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0005_auto_20190813_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True)),
                ('visualization', models.ImageField(blank=True, upload_to='attributes')),
            ],
        ),
    ]
