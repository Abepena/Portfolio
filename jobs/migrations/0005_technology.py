# Generated by Django 2.1.1 on 2018-10-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20181011_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete='CASCADE', related_name='technologies', to='jobs.Project')),
            ],
        ),
    ]
