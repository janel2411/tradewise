# Generated by Django 3.2 on 2024-06-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0004_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trades.category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='comment',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='comment',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trades.category'),
            preserve_default=False,
        ),
    ]
