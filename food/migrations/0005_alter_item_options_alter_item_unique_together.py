# Generated by Django 4.1.2 on 2022-11-25 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
