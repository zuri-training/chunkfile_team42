# Generated by Django 4.1 on 2022-08-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0004_documents_totalchunk_alter_documents_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
