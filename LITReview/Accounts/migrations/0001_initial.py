# Generated by Django 4.1.7 on 2023-02-15 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1238, verbose_name='Titre')),
                ('descritpion', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Utilisateur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]