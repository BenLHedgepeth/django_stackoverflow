# Generated by Django 3.2 on 2022-02-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_created_fk_on_Answer_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-score', '-date']},
        ),
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='type',
            field=models.CharField(default='', max_length=7),
            preserve_default=False,
        ),
    ]
