# Generated by Django 5.0.3 on 2024-03-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_alter_category_options_category_likes_category_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
