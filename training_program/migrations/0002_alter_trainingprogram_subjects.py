# Generated by Django 5.1.1 on 2024-10-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        ('training_program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprogram',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='programs', to='subject.subject'),
        ),
    ]
