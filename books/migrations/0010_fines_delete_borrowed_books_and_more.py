# Generated by Django 4.0.5 on 2022-07-06 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_borrowed_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.DeleteModel(
            name='borrowed_books',
        ),
        migrations.RenameField(
            model_name='borrower',
            old_name='book_num',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='issuedbook',
            old_name='book_num',
            new_name='book_name',
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='borrower',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
