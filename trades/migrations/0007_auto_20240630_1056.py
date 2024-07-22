# Generated by Django 3.2 on 2024-06-30 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0006_auto_20240630_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.RemoveField(
            model_name='post',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trades.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='trades.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='trades.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='trades.category'),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.profile')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='trades.comment')),
            ],
        ),
    ]