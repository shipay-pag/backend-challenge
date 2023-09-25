from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

def sql_query():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = """
        SELECT u."name", u.email, r.description AS role, c.description AS claim
        FROM users AS u
        JOIN roles AS r ON u.role_id = r.id
        LEFT JOIN user_claims AS uc ON u.id = uc.user_id
        LEFT JOIN claims AS c ON uc.claim_id = c.id
    """

    result = session.execute(query)

    data = []
    for row in result:
        data.append({
            "name": row[0],
            "email": row[1],
            "role": row[2],
            "claim": row[3]
        })

    session.close()
    engine.dispose()

    return data
