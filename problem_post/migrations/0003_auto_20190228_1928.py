# Generated by Django 2.1.5 on 2019-02-28 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem_post', '0002_auto_20190228_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemtopic',
            name='done',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='problemtopic',
            name='in_progress',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='problemtopic',
            name='performer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='performer', to=settings.AUTH_USER_MODEL),
        ),
    ]
