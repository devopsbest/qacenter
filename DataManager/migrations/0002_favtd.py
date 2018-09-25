# Generated by Django 2.0.3 on 2018-07-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavTd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.CharField(max_length=20, verbose_name='用户')),
                ('belong_td', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.TdInfo')),
            ],
            options={
                'verbose_name': '我收藏的事务',
                'db_table': 'Fav_Td',
            },
        ),
    ]
