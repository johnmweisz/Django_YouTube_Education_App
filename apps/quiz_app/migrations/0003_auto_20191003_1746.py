# Generated by Django 2.2.6 on 2019-10-03 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_auto_20190627_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='video_app.Video'),
        ),
    ]