import os
import time

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .utils.database_utils import migrate_to_db
from .utils.docker_utils import start_database_container
@pytest.fixture(scope='session',autouse=True)
def db_session() -> sessionmaker[Session]:
    container = start_database_container()
    time.sleep(3)
    TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
    engine = create_engine(TEST_DATABASE_URL)
    print(engine)

    with engine.begin() as connection:
        migrate_to_db(script_location="migrations",alembic_ini_path="alembic.ini",connection=connection,revision="head")

    SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)

    yield SessionLocal

    # container.stop()
    # container.remove()
    engine.dispose()