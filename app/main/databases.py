import os

DATABASES_DIR = 'db'
DATABASE_SUFFIX = '.db'


def get_db_name(filename: str):
    return filename.removesuffix(DATABASE_SUFFIX)


def is_database(filename: str):
    return filename.endswith(DATABASE_SUFFIX)


def get_databases():
    return list(map(get_db_name, filter(is_database, os.listdir(DATABASES_DIR))))


def get_database_schema(db_id):
    with open(f'{DATABASES_DIR}/ddl/{db_id}.ddl', 'r') as file:
        file_content = file.read()
    return file_content
