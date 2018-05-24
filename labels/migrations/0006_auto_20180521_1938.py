# Generated by Django 2.0.5 on 2018-05-21 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0005_auto_20180521_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='addon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='labels.Addon'),
        ),
        migrations.AlterField(
            model_name='label',
            name='bag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='labels.Bag'),
        ),
    ]
