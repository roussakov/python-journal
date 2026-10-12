from typing import Required
import uuid
from pydantic import BaseModel, ConfigDict, Field

from python_journal.schemas.tag import TagResponse

class EntryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    content: str
    tags: list[TagResponse]

class EntriesResponse(BaseModel):
    list: list[EntryResponse]

class CreateEntryRequest(BaseModel):
    content: str
    tags: list[str] = Field([])