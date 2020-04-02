# Generated by Django 3.0.4 on 2020-04-02 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(blank=True, max_length=100, null=True)),
                ('std_roll', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('std_class', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Students',
                'ordering': ['-id'],
                'unique_together': {('std_roll', 'std_class')},
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.BooleanField()),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='practice_api.Student')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
                'ordering': ['-id'],
                'unique_together': {('student', 'date')},
            },
        ),
    ]
