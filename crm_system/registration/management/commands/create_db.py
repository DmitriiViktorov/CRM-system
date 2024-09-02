from django.core.management.base import BaseCommand
import psycopg2
from psycopg2 import sql
from django.conf import settings
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = "Create database if it does not exist"

    def handle(self, *args, **options):
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST'] or 'localhost'

        try:
            connection = psycopg2.connect(
                dbname='postgres',
                user=db_user,
                password=db_password,
                host=db_host
            )
            connection.autocommit = True
            cursor = connection.cursor()

            cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db_name])
            exists = cursor.fetchone()

            if not exists:
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                self.stdout.write(self.style.SUCCESS(f"База данных '{db_name}' была успешно создана."))
            else:
                self.stdout.write(self.style.SUCCESS(f"База данных '{db_name}' уже присутствует на вашем устройстве."))

            cursor.close()
            connection.close()
        except OperationalError:
            self.stdout.write(self.style.ERROR("Ошибка подключения к PostgreSQL."))
