# Generated by Django 2.1.4 on 2018-12-18 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icallback_app', '0004_auto_20181217_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='calls', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='call',
            name='status',
            field=models.CharField(choices=[('OPERATOR_ANSWERED', 'OPERATOR_ANSWERED'), ('CLIENT_ANSWERED', 'CLIENT_ANSWERED'), ('NO_ANSWER', 'NO_ANSWER'), ('FAILED', 'FAILED')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='widget_key',
            field=models.CharField(blank=True, default=uuid.uuid1, max_length=140),
        ),
    ]
