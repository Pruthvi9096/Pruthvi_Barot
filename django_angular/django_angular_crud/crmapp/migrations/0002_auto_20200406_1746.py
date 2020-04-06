# Generated by Django 2.1.15 on 2020-04-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.FloatField()),
                ('unit', models.CharField(choices=[('g', 'Gram'), ('kg', 'Kilogram')], max_length=80)),
                ('note', models.TextField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='contact',
        ),
        migrations.DeleteModel(
            name='ActivityStatus',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='account',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='createdBy',
        ),
        migrations.DeleteModel(
            name='ContactSource',
        ),
        migrations.DeleteModel(
            name='ContactStatus',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
