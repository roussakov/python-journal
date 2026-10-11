
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from python_journal.models.base import Base

class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
    )
    content: Mapped[str]