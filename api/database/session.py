from sqlalchemy.orm import Session
from contextlib import contextmanager

from api.database.database import engine


class DBSessionContext(object):
    """
    Classe que define um contexto para gerenciamento de sessão do banco de dados.

    Métodos:
        - get_session_scope(): Retorna um escopo de sessão do banco de dados.
    """

    @contextmanager
    def get_session_scope(self):
        """
        Método para obter um escopo de sessão do banco de dados.

        Retorna:
            session (Session): Objeto de sessão do banco de dados.
        """
        engine.dispose()
        session = Session(bind=engine, autocommit=False, autoflush=False)
        with session.begin():
            try:
                yield session
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
