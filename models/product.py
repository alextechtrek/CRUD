from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from orm.setting import db


class Product(db.Model):
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
