import os

DATABASES_DIR = 'db'
DATABASE_SUFFIX = '.db'


def get_db_name(filename: str):
    return filename.removesuffix(DATABASE_SUFFIX)


def is_database(filename: str):
    return filename.endswith(DATABASE_SUFFIX)


def get_databases():
    return list(map(get_db_name, filter(is_database, os.listdir(DATABASES_DIR))))
