# Generated by Django 2.1.4 on 2018-12-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=140)),
                ('widget_key', models.CharField(blank=True, max_length=140)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
