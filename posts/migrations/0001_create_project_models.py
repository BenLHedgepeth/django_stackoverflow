# Generated by Django 3.2 on 2022-02-10 02:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('authors', '0002_create_project_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', related_query_name='comment', to='authors.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=75)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', related_query_name='question', to='authors.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to='authors.profile')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPageHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.GenericIPAddressField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='posts.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', related_query_name='question', to='posts.Tag'),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='authors.profile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', related_query_name='answer', to='authors.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]