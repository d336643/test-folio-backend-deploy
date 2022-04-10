# Generated by Django 4.0.3 on 2022-04-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('cash', models.FloatField()),
                ('budget', models.FloatField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_alive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'portfolio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('name', models.TextField()),
                ('group', models.TextField()),
            ],
            options={
                'db_table': 'stock',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('bankaccount', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('id_number', models.TextField()),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('time', models.DateTimeField()),
                ('price', models.FloatField()),
                ('portfolio', models.ForeignKey(db_column='portfolio', on_delete=django.db.models.deletion.CASCADE, to='engine.portfolio')),
                ('stock', models.ForeignKey(db_column='stock', on_delete=django.db.models.deletion.CASCADE, to='engine.stock')),
            ],
            options={
                'db_table': 'transaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Stockprice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('price', models.FloatField()),
                ('stock', models.ForeignKey(db_column='stock', on_delete=django.db.models.deletion.CASCADE, to='engine.stock')),
            ],
            options={
                'db_table': 'stockprice',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='owner',
            field=models.ForeignKey(db_column='owner', on_delete=django.db.models.deletion.CASCADE, to='engine.user'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('budget', models.FloatField()),
                ('cash', models.FloatField()),
                ('stop_limit', models.FloatField()),
                ('is_alive', models.BooleanField(default=True)),
                ('portfolio', models.ForeignKey(db_column='portfolio', on_delete=django.db.models.deletion.CASCADE, to='engine.portfolio')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='engine.user')),
            ],
            options={
                'db_table': 'follow',
                'managed': True,
            },
        ),
    ]
