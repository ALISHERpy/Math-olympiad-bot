# Generated by Django 3.2.9 on 2023-10-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20230911_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(blank=True, max_length=16)),
            ],
        ),
    ]
