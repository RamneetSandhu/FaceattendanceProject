# Generated by Django 3.2.5 on 2021-07-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]