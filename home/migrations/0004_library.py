# Generated by Django 2.2.2 on 2019-07-02 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, verbose_name='BOOK NAME')),
                ('author_name', models.CharField(max_length=30, verbose_name='AUTHOR NAME')),
                ('sut', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Student')),
            ],
        ),
    ]
