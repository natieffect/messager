# Generated by Django 3.2.18 on 2023-05-03 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('detail', models.TextField(blank=True)),
                ('send_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='client.account')),
                ('send_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resiver', to='client.account')),
            ],
            options={
                'ordering': ['send_to', 'send_from', 'detail', 'pub_date'],
            },
        ),
    ]
