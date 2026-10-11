import uuid
from pydantic import BaseModel, ConfigDict

class EntryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    content: str

class EntriesResponse(BaseModel):
    list: list[EntryResponse]

class CreateEntryRequest(BaseModel):
    content: str