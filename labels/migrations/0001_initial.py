# Generated by Django 2.0.5 on 2018-05-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('fnsku', models.CharField(max_length=10)),
                ('short_title', models.CharField(max_length=50)),
                ('bag_size', models.CharField(max_length=10)),
            ],
        ),
    ]