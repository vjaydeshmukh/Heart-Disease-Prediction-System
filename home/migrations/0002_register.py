# Generated by Django 2.2.1 on 2019-08-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('confirm_password', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
