# Generated by Django 2.2.1 on 2019-09-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passcet', '0011_auto_20190829_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='passcet_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_part', models.TextField(max_length=128)),
                ('status', models.TextField(max_length=128)),
                ('time', models.TextField(max_length=128)),
            ],
        ),
    ]
