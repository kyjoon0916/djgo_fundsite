# Generated by Django 3.2.5 on 2021-07-29 03:31

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='글제목')),
                ('contents', models.TextField(verbose_name='글내용')),
                ('tag', models.CharField(max_length=32, verbose_name='게시판종류')),
                ('write_dttm', models.DateTimeField(auto_now=True, verbose_name='마지막수정일')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('capital', models.PositiveIntegerField(default=0, verbose_name='펀딩금액')),
                ('userid', models.ForeignKey(db_column='writerid', on_delete=django.db.models.deletion.CASCADE, to='pybo.user', verbose_name='작성자')),
            ],
            options={
                'db_table': 'writing',
            },
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.PositiveIntegerField(default=0, verbose_name='포인트')),
                ('balance', models.PositiveIntegerField(default=0, verbose_name='잔액')),
                ('userid', models.ForeignKey(db_column='writer', on_delete=django.db.models.deletion.CASCADE, to='pybo.user', verbose_name='작성자')),
            ],
            options={
                'db_table': 'funding',
            },
        ),
    ]
