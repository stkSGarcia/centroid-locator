from typing import Optional

from sqlmodel import SQLModel, Session, select, Field

from app.config import ENGINE


class User(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    name: str
    password: str
    is_delete: int


def init_table():
    SQLModel.metadata.create_all(ENGINE)


def login(username, password) -> (int, str):
    with Session(ENGINE) as session:
        statement = select(User).where(User.username == username).where(User.is_delete == 0)
        user = session.exec(statement).first()
        if user is None:
            return -1, None
        elif user.password == password:
            return 1, user.username
        else:
            return 0, None


def register(username, name, password) -> bool:
    user = User(username=username, name=name, password=password, is_delete=0)
    with Session(ENGINE) as session:
        session.add(user)
        session.commit()
    return True
