# Generated by Django 3.2.18 on 2023-05-03 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myclient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=3)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('phoneb', models.CharField(blank=True, max_length=12, null=True)),
                ('coutry', models.CharField(choices=[('aa', 'Addis Ababa'), ('naz', 'Nazrēt'), ('god', 'Gonder'), ('mek', 'Mekele'), ('aws', 'Āwasa'), ('dd', 'Dire Dawa'), ('bah', 'Bahir Dar'), ('har', 'Harar'), ('jig', 'Jijiga'), ('aso', 'Āsosa'), ('gam', 'Gambēla'), ('sem', 'Semera')], max_length=3)),
            ],
            options={
                'ordering': ['first_name', 'middle_name', 'last_name', 'gender', 'email', 'coutry', 'pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('password', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.myclient', unique=True)),
            ],
            options={
                'ordering': ['user', 'password', 'pub_date'],
            },
        ),
    ]
