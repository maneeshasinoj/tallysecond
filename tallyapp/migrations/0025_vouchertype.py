# Generated by Django 4.0.4 on 2022-08-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0024_credit_delete_creditenote'),
    ]

    operations = [
        migrations.CreateModel(
            name='vouchertype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucherno', models.CharField(max_length=255)),
            ],
        ),
    ]
