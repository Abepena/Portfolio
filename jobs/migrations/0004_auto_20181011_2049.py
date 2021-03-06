# Generated by Django 2.1.1 on 2018-10-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-end_date']},
        ),
        migrations.AddField(
            model_name='project',
            name='demo_link',
            field=models.URLField(blank=True, null=True, verbose_name='Demo Link'),
        ),
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True, null=True, verbose_name='Github Link'),
        ),
    ]
