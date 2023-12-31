# Generated by Django 3.2.10 on 2022-03-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=20)),
                ('sex', models.BooleanField(default=False)),
                ('status', models.CharField(default='N/A', max_length=20)),
                ('remark', models.CharField(max_length=200)),
                ('update', models.DateField()),
                ('album', models.CharField(max_length=400)),
            ],
        ),
    ]
