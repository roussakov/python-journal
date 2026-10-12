
from __future__ import annotations
from typing import TYPE_CHECKING
import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from python_journal.models.base import Base

if TYPE_CHECKING:
    from python_journal.models.entry import Tag

class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
    )
    content: Mapped[str]
    tags: Mapped[list[Tag]] = relationship(
        secondary="entry_tags",
        back_populates="entries",
        passive_deletes=True,
    )