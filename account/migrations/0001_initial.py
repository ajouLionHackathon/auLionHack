# Generated by Django 3.1.1 on 2020-09-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=1, verbose_name='성별')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]