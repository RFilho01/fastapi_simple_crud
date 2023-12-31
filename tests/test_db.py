from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='roberto', password='password', email='roberto@teste.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'roberto'))

    assert user.username == 'roberto'
