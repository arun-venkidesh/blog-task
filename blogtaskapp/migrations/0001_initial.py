# Generated by Django 5.1 on 2024-08-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=255)),
                ('Date', models.CharField(max_length=255, null=True)),
                ('Author', models.CharField(max_length=50)),
            ],
        ),
    ]
