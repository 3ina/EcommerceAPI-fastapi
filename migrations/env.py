import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app import models
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

DEV_DATABASE_URL = os.environ.get("DEV_DATABASE_URL")
TEST_DATABASE_URL = os.environ.get("TEST_DATABASE_URL")

if DEV_DATABASE_URL:
    config.set_section_option("devdb", "sqlalchemy.url", DEV_DATABASE_URL)
else:
    raise ValueError("DEV_DATABASE_URL environment variable is not set.")

if TEST_DATABASE_URL:
    config.set_section_option("testdb", "sqlalchemy.url", TEST_DATABASE_URL)
else:
    raise ValueError("TEST_DATABASE_URL environment variable is not set.")
target_metadata = models.Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
