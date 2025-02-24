# Generated by Django 4.2.16 on 2025-02-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('src_ip', models.CharField(max_length=15)),
                ('dst_ip', models.CharField(max_length=15)),
                ('protocol', models.CharField(max_length=10)),
                ('src_port', models.IntegerField(blank=True, null=True)),
                ('dst_port', models.IntegerField(blank=True, null=True)),
                ('payload', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
