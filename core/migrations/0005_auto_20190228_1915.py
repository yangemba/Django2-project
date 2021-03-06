# Generated by Django 2.1.5 on 2019-02-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190228_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='messages',
            field=models.ManyToManyField(blank=True, to='message.Message'),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='total_money_spend',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='masterprofile',
            name='messages',
            field=models.ManyToManyField(blank=True, to='message.Message'),
        ),
        migrations.AlterField(
            model_name='masterprofile',
            name='score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='masterprofile',
            name='total_money_earn',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
