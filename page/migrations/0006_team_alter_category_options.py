# Generated by Django 4.2.6 on 2023-10-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_rename_button_product_button_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='uploads/')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
