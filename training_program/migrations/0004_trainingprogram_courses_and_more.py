# Generated by Django 5.1.1 on 2024-10-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('subject', '0001_initial'),
        ('training_program', '0003_alter_trainingprogram_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingprogram',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='training_programs', to='course.course'),
        ),
        migrations.AlterField(
            model_name='trainingprogram',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='programs', to='subject.subject'),
        ),
    ]
