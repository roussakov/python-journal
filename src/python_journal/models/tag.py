
from __future__ import annotations
from typing import TYPE_CHECKING
import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from python_journal.models.base import Base

if TYPE_CHECKING:
    from python_journal.models.entry import Entry

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
    )

    entries: Mapped[list[Entry]] = relationship(
        secondary="entry_tags",
        back_populates="tags",
        passive_deletes=True,
    )