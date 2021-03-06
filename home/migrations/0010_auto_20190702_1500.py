# Generated by Django 2.2.2 on 2019-07-02 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_friends_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=100, null=True, verbose_name='Book')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=20, verbose_name='Section')),
                ('Student', models.ManyToManyField(to='home.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='library',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='library',
            name='book_name',
        ),
        migrations.RemoveField(
            model_name='library',
            name='sut',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_sal',
        ),
        migrations.AddField(
            model_name='library',
            name='library_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Library'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
        migrations.AddField(
            model_name='section',
            name='advisor',
            field=models.OneToOneField(null=True, on_delete=True, to='home.Teacher'),
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(null=True, to='home.Book'),
        ),
    ]
