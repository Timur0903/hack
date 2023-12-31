# Generated by Django 4.2.3 on 2023-07-25 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myzloo', '0004_remove_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='activation_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='myzloo.musictrack'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myzloo.musictrack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_tracks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'track')},
            },
        ),
    ]
