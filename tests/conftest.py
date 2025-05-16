import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from app.adapters.unit_of_work import SqlAlchemyUnitOfWork
from framework_drivers.orm.base import Base


@pytest.fixture(scope="function")
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    clear_mappers()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def uow(session):
    return SqlAlchemyUnitOfWork(session)
