# Generated by Django 3.1.4 on 2021-03-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extendedusers',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
