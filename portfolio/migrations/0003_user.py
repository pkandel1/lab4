# Generated by Django 2.1 on 2022-03-16 19:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_investment_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
