# Generated by Django 4.1.3 on 2023-01-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_is_deleted_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]