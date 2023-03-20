# Generated by Django 4.1.7 on 2023-03-15 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('ticket', '0002_alter_volunteerticket_agreement_template_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
                ('volunteer_ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.volunteerticket')),
            ],
        ),
    ]
