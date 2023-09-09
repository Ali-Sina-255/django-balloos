# Generated by Django 4.2.4 on 2023-09-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balloon', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='media/team/')),
                ('phone_number', models.IntegerField(max_length=15)),
            ],
        ),
    ]