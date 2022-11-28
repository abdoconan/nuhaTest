# Generated by Django 4.0.8 on 2022-11-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('train_type_name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]