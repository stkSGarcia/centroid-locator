from typing import Optional

from sqlmodel import SQLModel, Session, select, Field

from app.config import ENGINE


class User(SQLModel, table=True):
    username: Optional[str] = Field(default=None, primary_key=True)
    name: str
    passwd: str
    is_delete: int


def init_table():
    SQLModel.metadata.create_all(ENGINE)


def login(username, passwd) -> (int, str):
    with Session(ENGINE) as session:
        statement = select(User).where(User.username == username).where(User.is_delete == 0)
        user = session.exec(statement).first()
        if user is None:
            return -1, None
        elif user.passwd == passwd:
            return 1, user.username
        else:
            return 0, None


def register(username, name, passwd) -> bool:
    user = User(username=username, name=name, passwd=passwd, is_delete=0)
    with Session(ENGINE) as session:
        session.add(user)
        session.commit()
    return True
