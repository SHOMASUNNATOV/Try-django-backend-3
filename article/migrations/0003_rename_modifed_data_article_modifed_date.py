# Generated by Django 4.1.3 on 2022-12-08 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_modifed_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='modifed_data',
            new_name='modifed_date',
        ),
    ]
