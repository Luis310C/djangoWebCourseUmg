# Generated by Django 3.1 on 2020-11-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Climatic', '0004_auto_20201104_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Id_Usuario',
            field=models.IntegerField(),
        ),
    ]
