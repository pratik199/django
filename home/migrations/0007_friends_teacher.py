# Generated by Django 2.2.2 on 2019-07-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='Teacher',
            field=models.ManyToManyField(to='home.Teacher'),
        ),
    ]
