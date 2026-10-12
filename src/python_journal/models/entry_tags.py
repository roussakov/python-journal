
import uuid
from sqlalchemy import Column, ForeignKey, Table
from python_journal.models.base import Base


entry_tags = Table(
    "entry_tags", 
    Base.metadata,
    Column(
        "entry_id",
        ForeignKey("entries.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "tag_id",
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True
    ))

