# Generated by Django 4.0.5 on 2022-07-05 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrower',
            options={'verbose_name_plural': 'borrowers'},
        ),
        migrations.AlterModelOptions(
            name='issuedbook',
            options={'verbose_name_plural': 'issuedbooks'},
        ),
    ]