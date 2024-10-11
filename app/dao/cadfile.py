from typing import Optional
from warnings import catch_warnings

from sqlmodel import SQLModel, Session, select, Field

from app.config import ENGINE


class Cadfile(SQLModel, table=True):
    __tablename__ = "cad_info"
    id: Optional[int] = Field(default=None, primary_key=True)
    # username: Optional[str] = Field(default=None, primary_key=True)
    name: str
    location: str
    description: str
    username: str
    is_delete: int


def init_table():
    SQLModel.metadata.create_all(ENGINE)


# TODO: 当前先展示全部后期支持模糊筛选。
def list(name: str, createuser: int) -> (int, str):
    with Session(ENGINE) as session:
        statement = select(Cadfile).where(Cadfile.is_delete == 0)
        cadFileList = session.exec(statement).all()
        if cadFileList is None:
            return -1, None
        else:
            return 0, cadFileList


def add(name: str, description: str, username:str, location:str) -> bool:
    cad_file = Cadfile(name=name, description=description, username=username, location=location, is_delete=0)
    try:
        with Session(ENGINE) as session:
            session.add(cad_file)
            session.commit()
    except Exception as e:
        print(repr(e))
    return True

