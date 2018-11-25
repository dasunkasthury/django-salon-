# Generated by Django 2.1.3 on 2018-11-25 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_status', models.CharField(choices=[('PENDING', 'pending'), ('CONFIRMED', 'confirmed')], default='PENDING', max_length=250)),
                ('payment', models.IntegerField()),
                ('payment_status', models.CharField(choices=[('PENDING', 'pending'), ('PAYED', 'payed')], default='PENDING', max_length=250)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer_name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('value', models.IntegerField()),
                ('type', models.CharField(choices=[('Stylist', 'Stylist'), ('Educator', 'Educator')], default='Stylist', max_length=250)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('FULL-TIME', 'full-time'), ('PART-TIME', 'part-time')], default='FULL-TIME', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salon_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('evening', models.CharField(choices=[('FREE', 'free'), ('BUSY', 'busy')], default='FREE', max_length=250)),
                ('morning', models.CharField(choices=[('FREE', 'free'), ('BUSY', 'busy')], default='FREE', max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='freelancer',
            name='time_slot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Timeslot'),
        ),
        migrations.AddField(
            model_name='book',
            name='freelancer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Freelancer'),
        ),
        migrations.AddField(
            model_name='book',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Job'),
        ),
        migrations.AddField(
            model_name='book',
            name='salon_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Salon'),
        ),
    ]
