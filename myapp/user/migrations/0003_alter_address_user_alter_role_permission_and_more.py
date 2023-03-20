# Generated by Django 4.1.7 on 2023-03-15 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_event_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.permission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.role'),
        ),
    ]
