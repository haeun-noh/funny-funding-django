# Generated by Django 4.2.13 on 2024-06-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funfun', '0002_alter_user_email_alter_user_nickname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='company',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
