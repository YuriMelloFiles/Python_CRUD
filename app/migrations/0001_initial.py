# Generated by Django 4.0.3 on 2022-03-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=100)),
                ('concessionaria', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=100)),
            ],
        ),
    ]
