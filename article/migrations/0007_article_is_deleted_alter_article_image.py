# Generated by Django 4.1.3 on 2022-12-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_rename_created_time_article_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, help_text='2MB dan oshmasin!', null=True, upload_to='articles'),
        ),
    ]
