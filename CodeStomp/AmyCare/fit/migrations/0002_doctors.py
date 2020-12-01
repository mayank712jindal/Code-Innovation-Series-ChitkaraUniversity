# Generated by Django 3.1.3 on 2020-11-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doc_id', models.AutoField(primary_key=True, serialize=False)),
                ('doc_name', models.CharField(default='', max_length=100)),
                ('doc_category', models.CharField(default='', max_length=100)),
                ('doc_phone', models.IntegerField()),
                ('doc_address', models.CharField(default='', max_length=500)),
                ('doc_idProof', models.ImageField(default='', upload_to='fit/doctors')),
            ],
        ),
    ]