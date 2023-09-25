import pytest
from sqlalchemy import create_engine
from user_sqlquery import sql_query
from config import DATABASE_URL

@pytest.fixture
def database_engine():
    engine = create_engine(DATABASE_URL)
    return engine

def test_get_user_permissions(database_engine):
    result = sql_query(database_engine)
    assert isinstance(result, list)
    assert len(result) > 0
