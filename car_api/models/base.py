from sqlalchemy.orm import usernameMapped, mapped_column

from car_api.models import Base

class user_base:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    email: Mapped[str]
