# Generated by Django 3.2.7 on 2021-10-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=30)),
                ('stuemail', models.EmailField(max_length=30)),
                ('stupass', models.CharField(max_length=30)),
            ],
        ),
    ]