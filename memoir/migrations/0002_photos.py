# Generated by Django 4.0.2 on 2022-02-27 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memoir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(max_length=100)),
                ('img_description', models.TextField()),
                ('image', models.ImageField(upload_to='Images/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('img_categories', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-img_title'],
            },
        ),
    ]
