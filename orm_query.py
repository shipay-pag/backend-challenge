from models import Session, User, Role, Claim, UserClaim

def orm_query():
    session = Session()

    data = []
    users = session.query(User,Role, Claim).join(Role, User.role_id == Role.id).outerjoin(UserClaim, User.id == UserClaim.user_id).outerjoin(Claim, UserClaim.claim_id == Claim.id).all()

    for user, role, claim in users:
        user_data = {
            "name": user.name,
            "email": user.email,
            "role": role.description,
            "permissions": claim.description if claim else None

        }

        data.append(user_data)

    session.close()
    return data
