# Generated by Django 2.2.4 on 2022-06-29 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_message_for_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='for_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usermessages', to='app_one.User'),
        ),
    ]
