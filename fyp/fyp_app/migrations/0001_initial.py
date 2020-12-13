# Generated by Django 3.1.4 on 2020-12-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('urgent', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]