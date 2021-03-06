# Generated by Django 3.0.6 on 2020-06-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='pics')),
                ('relyear', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('ratings', models.CharField(max_length=5)),
                ('category', models.ManyToManyField(to='movie.Category')),
            ],
        ),
    ]
