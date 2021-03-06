# Generated by Django 3.2.5 on 2021-08-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
                ('user_type', models.CharField(max_length=2)),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
