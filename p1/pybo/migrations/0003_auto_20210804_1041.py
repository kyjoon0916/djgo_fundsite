# Generated by Django 3.2.5 on 2021-08-04 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='userid',
            field=models.ForeignKey(db_column='writer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='writing',
            name='userid',
            field=models.ForeignKey(db_column='writerid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]