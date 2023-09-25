import pytest
from sqlalchemy.orm import sessionmaker ,create_engine
from orm_query import orm_query
from config import DATABASE_URL


engine = create_engine(DATABASE_URL)

@pytest.fixture
def database_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def test_get_user_permissions_orm(database_session):
    result = orm_query(database_session)
    assert isinstance(result, list)
    assert len(result) > 0
