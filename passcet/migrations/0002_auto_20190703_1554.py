# Generated by Django 2.2.1 on 2019-07-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passcet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passcet_user',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='passcet_user',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
