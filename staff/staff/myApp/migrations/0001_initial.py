# Generated by Django 4.2.3 on 2023-11-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile_no', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
