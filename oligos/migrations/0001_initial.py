# Generated by Django 2.2.3 on 2019-08-28 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Oligo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('sequence', models.CharField(blank=True, max_length=200)),
                ('details', models.CharField(blank=True, max_length=800)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=True)),
                ('primer_position', models.CharField(blank=True, choices=[('S', 'Sense'), ('A', 'Antisense'), ('U', 'Unspecified')], default='U', max_length=2)),
                ('gene_locus', models.CharField(blank=True, max_length=120)),
                ('organism', models.CharField(blank=True, max_length=80)),
                ('primer_partner', models.CharField(blank=True, max_length=120)),
                ('company', models.CharField(blank=True, max_length=80)),
                ('concentration', models.FloatField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=80)),
                ('usages', models.ManyToManyField(blank=True, to='oligos.Usage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
