# Generated by Django 3.0.4 on 2020-05-26 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0012_quotewarehouse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotewarehouse',
            old_name='timeStamp',
            new_name='timestamp',
        ),
    ]
