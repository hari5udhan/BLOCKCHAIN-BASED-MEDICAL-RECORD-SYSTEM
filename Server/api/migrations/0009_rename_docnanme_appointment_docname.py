# Generated by Django 4.0.2 on 2022-02-22 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_appointment_docnanme_appointment_patname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='docNanme',
            new_name='docName',
        ),
    ]
