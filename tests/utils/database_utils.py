import os

import alembic.config
from alembic import command
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def migrate_to_db(
        script_location : str,
        alembic_ini_path : str ="alembic.ini",
        connection=None,
        revision : str ="head"
        ):
    """
       Apply database migrations using Alembic.

       Args:
           script_location (str): Path to the Alembic script directory.
           alembic_ini_path (str): Path to the Alembic configuration file.
           connection: Optional database connection object. If provided, Alembic will use this connection.
           revision (str): The revision to upgrade to (default is "head").
       """

    try:
        alembic_cfg = alembic.config.Config(alembic_ini_path)
        alembic_cfg.set_main_option("script_location", script_location)

        if connection is not None:
            alembic_cfg.attributes["connection"] = connection
            logger.info("Using provided database connection for migrations.")
        else:
            # Use the testdb section in alembic.ini
            TEST_DATABASE_URL = os.environ.get('TEST_DATABASE_URL')
            alembic_cfg.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
            logger.info("Using testdb configuration from alembic.ini.")

        logger.info(f"Applying migrations to revision: {revision}")
        command.upgrade(alembic_cfg, revision)
        logger.info("Migrations applied successfully.")
    except Exception as e:
        logger.error(f"Failed to apply migrations: {e}")
        raise

