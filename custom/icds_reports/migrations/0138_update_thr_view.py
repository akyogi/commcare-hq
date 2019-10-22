# Generated by Django 1.11.16 on 2019-10-10

from django.db import migrations

from corehq.sql_db.operations import RawSQLMigration


migrator = RawSQLMigration(('custom', 'icds_reports', 'migrations', 'sql_templates', 'database_views'))


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0138_add_db_index_inactive_aww'),
    ]

    operations = [migrator.get_migration('thr_report_view.sql')]
