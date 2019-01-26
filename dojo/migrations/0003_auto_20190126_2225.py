# Generated by Django 2.1.5 on 2019-01-26 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0002_auto_20190126_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(choices=[('A', 'A서버'), ('B', 'B서버'), ('C', 'C서버')], max_length=10)),
                ('username', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gameuser',
            unique_together={('server_name', 'username')},
        ),
    ]