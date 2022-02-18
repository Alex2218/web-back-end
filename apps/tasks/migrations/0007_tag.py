# Generated by Django 3.0.6 on 2020-10-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25)),
                ('color', models.CharField(default='424244', max_length=6)),
                ('tasks', models.ManyToManyField(blank=True, to='tasks.Task')),
            ],
        ),
    ]
