# Generated by Django 4.0.5 on 2022-06-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
