# Generated by Django 3.1.6 on 2021-02-05 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='description',
            field=models.TextField(null=True),
        ),
    ]